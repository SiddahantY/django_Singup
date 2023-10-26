from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from loginsys import settings
from django.core.mail import send_mail

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
            messages.error(request,"Username already taken")
            return redirect("Home")

        if User.objects.filter(email=email):
            messages.error(request,"email already registered")
            return redirect("Home")
        
        if len(username)>10:
            messages.error(request,"username should be less than 10 characters")

        if pass1 != pass2:
            messages.error(request,"password didn't match")
        
        if not username.isalnum():
            messages.error(request,"username should be in alphabets and digits")
            return redirect('Home')

        my_user=User.objects.create_user(username,email,pass1)
        my_user.first_name=fname
        my_user.last_name=lname

        my_user.save()

        messages.success(request,"Your account has been successfully created")

        # welcome email
        subject='welcome to login system'
        message="hello" + fname +"\n Thank u for visiting our website we have sent you a confirmation email, please confirm your email address in order to activate your account.\n\n Thanking you\nSiddahant Yadav"
        from_email=settings.EMAIL_HOST_USER
        to_list= [my_user.email]
        send_mail(subject, message, from_email, to_list, fail_silently=True)



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
    logout(request)
    messages.success(request,"you have logged out successfully")
    return redirect('Home')

