from django.shortcuts import render
from login.models import Login
from Shop.models import Shop

# Create your views here.


def shop(request):
    if request.method== 'POST':
        obb=Shop()
        obb.shop_name=request.POST.get('shop')
        obb.location=request.POST.get('location')
        obb.email=request.POST.get('email')
        obb.phone=request.POST.get('phone')
        obb.password=request.POST.get('password')
        obb.save()

        obj=Login()
        obj.email=obb.email
        obj.password=obb.password
        obj.type="shop"
        obj.u_id=obb.shop_id
        obj.save()
    return render(request,'Shop/Render_register.html')