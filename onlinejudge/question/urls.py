from django.urls import path

from . import views

urlpatterns = [
    path('MINIMUMJUMPS', views.solve, name = 'solve'),
]