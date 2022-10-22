from email import message
import http
from http.client import HTTPResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User, auth

# Create your views here.

def index(request):
     prop = Activites.objects.all()
     dire = Directors.objects.all()
     revi = Review.objects.all()
     expe = Experience.objects.all()

     return render(request, 'index.html',  {'Activites': prop,'Reviews':revi,'Directors':dire, 'Experience':expe})

def about(request):
     return render(request, 'about.html',)

def contact(request):
     return render(request, 'contact.html',)

def signup(request):
     if request.method=='POST':
      username = request.POST['username']
      firstName = request.POST['firstname']
      lastName = request.POST['lastname']
      password = request.POST['password1']
      email = request.POST['email']
      repeatPassword = request.POST['password2']
      if(password == repeatPassword):
        user = User.objects.create_user(username=username,first_name=firstName, last_name=lastName, password=password, email=email)
        user.save();
        return redirect('/login')
      else:
          messages.info(request,'Password does not match')
          return redirect('/signup')
     else:
      return render(request, 'sign up.html',)

def login(request):
     if request.method =='POST':
          username = request.POST['username']
          password = request.POST['password']
          user = auth.authenticate(username=username, password=password)
          if user is not None:
               auth.login(request,user)
               return redirect('/')
          else:
               messages.info(request, 'No such user')
               return redirect('/login')
     else:
      return render(request, 'log in.html',) 

def logout(request):
     auth.logout(request)
     return redirect('/')
