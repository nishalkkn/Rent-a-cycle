from django.shortcuts import render
from pip._vendor.six import b
from booking.models import Booking
from distance_tracking.models import DistanceTracking
# Create your views here.


def add_distance_travelled(request,):
    ss= request.session["uid"]
    obx=Booking.objects.filter(user_id=ss)
    context={
        'a':obx
    }

    if request.method=='POST':
        obb=DistanceTracking()
        obb.booking_id =request.POST.get('booking_id')
        obb.start_point =request.POST.get('st_point')
        obb.end_point =request.POST.get('end_point')
        obb.distance =request.POST.get('distance')
        obb.save()
    return render(request,'distance_tracking/add_distance_travelled.html',context)

def view_distance_travelled_render(request):
    ss= request.session["uid"]
    obb = DistanceTracking.objects.filter(booking__cycle__render_id=ss)
    context = {
        'a': obb
    }
    return render(request,'distance_tracking/view_distance_travelled_render.html',context)