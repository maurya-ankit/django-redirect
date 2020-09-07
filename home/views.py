from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from main.models import shorten,UserShort
from django.views import View

# Create your views here.


# @login_required(login_url='/login/')
def index(request):
    if request.user.is_authenticated:
        query = UserShort.objects.filter(user=request.user).order_by('-pk')
        context = {'query':query}
    else:
        query = shorten.objects.all().order_by('-pk')
        context = {'query':query}

    return render(request,'index.html',context)


class short(View):
    def get(self,request):
        if request.user.is_authenticated:
            context={}
            return render(request,'usershort.html',context)
        else:
            context={}
            return render(request,'shorten.html',context)
    def post(self,request):
        err_msg = None
        if request.user.is_authenticated:
            url = request.POST.get('url')
            shorturi = request.POST.get('shorturl')
            if url== "" or shorturi == "":
                err_msg = "All Fields are Required!"
                context = {'err_msg':err_msg}
            elif UserShort.objects.filter(user=request.user,shorturi=shorturi):
                err_msg="A short url with this name already exist. Try another"
                context = {'err_msg':err_msg}
            if err_msg:
                return render(request,'usershort.html',context)
            else:
                object=UserShort()
                object.uri=url
                object.shorturi=shorturi
                object.user = request.user
                object.save()
                return redirect('home:index')
        else:
            url = request.POST.get('url')
            if url=="":
                err_msg = "All Fields are Required!"
                context = {'err_msg':err_msg}
            if err_msg:
                return render(request,'shorten.html',context)
            else:
                object=shorten()
                object.uri=url
                object.save()
                return redirect('home:index')