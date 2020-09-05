from django.shortcuts import render,redirect
from .models import shorten
import http.server
import requests
from urllib.parse import unquote, parse_qs
from django.views import View
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='/login/')
def index(request):
    query = shorten.objects.all()
    context = {'query':query}

    return render(request,'index.html',context)

def Home(request,token):
    res = shorten.objects.get(shorturi =token).uri
    return redirect(res)

class short(View):
    def get(self,request):
        context={}
        return render(request,'shorten.html',context)
    def post(self,request):
        url = request.POST.get('url')
        print(type(url))
        object=shorten()
        object.uri=url
        object.save()
        context = {
            'shorturi':object.shorturi,
            'uri':object.uri,
        }
        return redirect(index)
    
    