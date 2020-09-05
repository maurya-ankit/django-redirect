

# Create your views here.
from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.models import User


# Create your views here.
def register(response):
    if response.method == "POST":
	    form = RegisterForm(response.POST)
	    if form.is_valid():
	        form.save()

	    return redirect("/")
    else:
	    form = RegisterForm()
	    totalUser=User.objects.count()
    return render(response, "register/register.html", {"form":form,'total':totalUser})
