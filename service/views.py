from django.shortcuts import render
from service.models import Service

# Create your views here.

def add_service(request):
    ss= request.session["uid"]
    if request.method=="POST":
        obb=Service()
        obb.render_id=ss
        obb.service=request.POST.get('service')
        obb.charge=request.POST.get('charge')
        obb.save()
    return render(request,'service/add_service.html')

def view_service_public(request):
    obb = Service.objects.all()
    context = {
        'a': obb
    }
    return render(request,'service/view_services_public.html',context)

def view_service_user(request):
    obb = Service.objects.all()
    context = {
        'a': obb
    }
    return render(request,'service/view_services_user.html',context)

def viw_service_admin(request):
    obb = Service.objects.all()
    context = {
        'a': obb
    }
    return render(request,'service/view_service_admin.html',context)