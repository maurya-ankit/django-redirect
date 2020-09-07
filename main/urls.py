from django.contrib import admin
from django.urls import path
from .views import homepage,homepageauth
from django.contrib.auth.models import User

urlpatterns = [
    path('<str:token>',homepage),
    path('<str:user>/<str:token>',homepageauth)
    
]
