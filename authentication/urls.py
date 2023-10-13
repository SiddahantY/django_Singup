from django.contrib import admin
from django.urls import path
from . import views
from .views import Home,Signup,Signin,Signout

urlpatterns = [
    path('Home/', Home, name='Home'),
    path('Signup/',Signup,name='Signup'),
    path('Signin/',Signin,name='Signin'),
    path('Signout/',Signout,name='Signout'),
]
