from django.shortcuts import render,redirect, get_object_or_404
from .models import shorten,UserShort
from django.views import View
from django.contrib.auth.decorators import login_required
# Create your views here.




def homepage(request,token):
    try:
        try:
            res=shorten.objects.filter(shorturi=token)[0].uri
            obj=shorten.objects.filter(shorturi=token)[0]
            newcount=int(obj.count)+1
            obj.count=newcount
            obj.save()

        except:
            res=UserShort.objects.filter(shorturi=token)[0].uri
            obj=UserShort.objects.filter(shorturi=token)[0]
            newcount=int(obj.count)+1
            obj.count=newcount
            obj.save()

    except:
        return redirect(f'/{token}/')
    return redirect(res)

    
    