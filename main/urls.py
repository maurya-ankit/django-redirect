from django.contrib import admin
from django.urls import path
from .views import Home,index,short
urlpatterns = [
    path('short',short.as_view()),
    #path('<str:token>',Home),
    path('',index,name='index'),

]
