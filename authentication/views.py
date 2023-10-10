from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages

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

        my_user=User.objects.create_user(username,email,pass1)
        my_user.first_name=fname
        my_user.last_name=lname

        my_user.save()

        messages.success(request,"Your account has been successfully created")
        return redirect("Signin")
    else:    
        return render(request,"Signup.html")

def Signin(request):
    return render(request,"Signin.html")

def Signout(request):
    pass
