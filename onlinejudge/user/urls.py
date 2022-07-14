from django.urls import path

from . import views

urlpatterns = [
    path('login', views.signin_, name = 'signin_'),
    #path('home', views.home, name = 'home'), #user profile page
    path('signup', views.signup_, name = 'signup_'),
    path('create', views.signup, name = 'signup'),
    path('logout', views.logout, name = 'logout'),
    #path('auth', views.auth, name = 'auth'),
]