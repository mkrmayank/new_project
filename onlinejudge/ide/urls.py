from django.urls import path

from . import views

urlpatterns = [
    path('runcode', views.runcode, name = 'code'),
]