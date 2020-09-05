from django.contrib import admin
from django.urls import path
from .views import Home,index,short
urlpatterns = [
    path('',index,name='index'),
    path('short',short.as_view()),
    path('<str:token>',Home),
    

]
