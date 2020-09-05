from django.contrib import admin
from django.urls import path
from .views import index,short

app_name = 'home'
urlpatterns = [
    path('',index,name='index'),
    path('short/',short.as_view(),name='short'),
    

]
