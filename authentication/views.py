from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login


def Home(request):
    return render(request,'index.html')

def Signup(request):
    if request.method == "POST":
        
    #   username = request.POST.get("username")
        username =request.POST["username"]
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        email = request.POST["email"]
        pass1 = request.POST["pass2"]
        pass2 = request.POST["pass2"]
        
        #check if username is already taken
        if User.objects.filter(username=username).exists():
            return HttpResponse('Username is already taken. Please choose a different username.')

        my_user=User.objects.create_user(username,email,pass1)
        my_user.first_name=fname
        my_user.last_name=lname

        my_user.save()

        messages.success(request,"Your account has been successfully created")
        return redirect("Signin")
    else:    
        return render(request,"Signup.html")

def Signin(request):
    if request.method=="POST":
        username=request.POST["username"]
        pass1=request.POST["pass1"]

        user=authenticate(username=username,password=pass1)
        
        if user is not None:
            login(request,user)
            fname=user.first_name
            return render(request,"index.html",{"fname":fname})
        else:
            messages.error(request,"Invalid credentials")

            return redirect("Home")
        
    return render(request,"Signin.html")


def Signout(request):
    pass
