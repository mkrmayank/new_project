from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.


def signin_(request):
    return render(request, 'oj/signin.html')


def signup_(request):
    return render(request, 'oj/signup.html')


def create(request):

    if request.method == "POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.info(request,'Username already taken')
            return redirect('http://localhost:8000/oj/user/signup')
        else:
            user=User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name)
            user.save()
            messages.info(request, "User created")
            return redirect('http://localhost:8000/oj/user/login')
    
    else:
        return e


def login(request):
    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('http://localhost:8000/oj/')
        
        else:
            messages.info(request, "Invalid Credentials")
            return redirect('http://localhost:8000/oj/user/login')
        

    else:
        return render(request, 'register.html')


def logout(request):
    auth.logout(request)
    return render(request, 'signin.html')