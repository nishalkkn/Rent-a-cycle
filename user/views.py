from django.shortcuts import render
from user.models import User
from login.models import Login

# Create your views here.

def user(request):
    if request.method== 'POST':
        obb=User()
        obb.name=request.POST.get('name')
        obb.email=request.POST.get('email')
        obb.phone=request.POST.get('phone')
        obb.password=request.POST.get('password')
        obb.save()

        obj = Login()
        obj.email = obb.email
        obj.password = obb.password
        obj.type = "user"
        obj.u_id = obb.user_id
        obj.save()
    return render(request,'user/user_register.html')
