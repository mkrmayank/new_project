from django.shortcuts import render

# Create your views here.


def register_user(request):
    return render(request, 'signup.html')


def login_user(request):
    return render(request, 'signin.html')

