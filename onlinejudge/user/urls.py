from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    #path('home', views.home, name = 'home'), #user profile page
    path('createuser', views.createuser, name = 'createuser'),
    #path('auth', views.auth, name = 'auth'),
]