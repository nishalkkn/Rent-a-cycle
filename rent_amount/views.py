from django.shortcuts import render
from rent_amount.models import RentAmount
from distance_tracking.models import DistanceTracking
from booking.models import Booking
# Create your views here.


def add_rent_amount_render(request,idd):
    obx=DistanceTracking.objects.get(distance_tracking_id=idd)
    context={
        'a':obx
    }

    if request.method=="POST":
        obb=RentAmount()
        obb.distance_tracking_id=idd
        obb.amount=request.POST.get('amount')
        obb.save()
    return render(request,'rent_amount/add_rent_amount.html')

def view_rent_amount_admin(request):
    obb = RentAmount.objects.all()
    context = {
        'a': obb
    }
    return render(request,'rent_amount/view_rent_amount_admin.html',context)


def view_rent_amount_user(request):
    ss= request.session["uid"]
    obb = RentAmount.objects.filter(distance_tracking__booking__user_id=ss)
    context = {
        'a': obb
    }
    return render(request,'rent_amount/view_rent_amount_user.html',context)

