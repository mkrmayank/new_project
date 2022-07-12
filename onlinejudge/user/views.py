from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'signin.html')


def createuser(request):
    return render(request, 'signup.html')


def createuser(request):

    if request.method== "POST":
        first_name=request.POST['first_name']
        laste_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        if Users.object.filter(username=username).exists():
            message.info(request,'Username not available')
            return render(request, 'signup.html')
        else:
            user=User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name)
    
    return redirect()
