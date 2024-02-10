from django.shortcuts import render
from cycle.models import Cycle
from feedback.models import Feedback
# Create your views here.

def admin(request):
    obb = Cycle.objects.all()
    obj = Feedback.objects.all()
    context = {
        'a': obb,
        'b': obj
    }
    return render(request,'temp/admin.html',context)

def public(request):
    obb=Cycle.objects.all()
    obj=Feedback.objects.all()
    context={
        'a':obb,
        'b':obj
    }
    return render(request,'temp/public.html',context)

def shop(request):
    ss=request.session["uid"]
    obb = Cycle.objects.filter(render__shop_id=ss)
    obj = Feedback.objects.filter(render__shop_id=ss)
    context = {
        'a': obb,
        'b': obj
    }
    return render(request,'temp/shop.html',context)

def user(request):
    obb = Cycle.objects.all()
    obj = Feedback.objects.all()
    context = {
        'a': obb,
        'b': obj
    }
    return render(request,'temp/user.html',context)

def home_usr(request):
    return render(request,'temp/home_usr.html')

def home_shop(request):
    return render(request,'temp/home_shop.html')

def home_admin(request):
    return render(request,'temp/home_admin.html')


def home_public(request):
    return render(request,'temp/home_public.html')
