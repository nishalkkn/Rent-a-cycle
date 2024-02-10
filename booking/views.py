from django.shortcuts import render
from booking.models import Booking
from cycle.models import Cycle

# Create your views here.

def book_cycle(request,idd):
    ss= request.session["uid"]
    obj = Cycle.objects.get(cycle_id=idd)
    context = {
        'x': obj
    }
    if request.method=='POST':
        obb=Booking()
        obb.cycle_id=idd
        obb.user_id=ss
        obb.date=request.POST.get('date')
        obb.time=request.POST.get('time')
        obb.status="pending"
        obb.save()
    return render(request,'booking/book_cycle.html',context)


def manage_booking_render(request):
    ss= request.session["uid"]
    obb=Booking.objects.filter(cycle__render__shop_id=ss)
    context={
        'a':obb
    }
    return render(request,'booking/manage_booking_render.html',context)

def view_booking_status(request):
    ss= request.session["uid"]
    obb = Booking.objects.filter(user_id=ss)
    context = {
        'a': obb
    }
    return render(request,'booking/view_booking _status_user.html',context)


def approve(request,idd):
    obb=Booking.objects.get(booking_id=idd)
    obb.status="Approved"
    obb.save()
    return manage_booking_render(request)

def reject(request,idd):
    obb=Booking.objects.get(booking_id=idd)
    obb.status="Rejected"
    obb.save()
    return manage_booking_render(request)