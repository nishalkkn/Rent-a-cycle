from django.shortcuts import render
from payment.models import Payment
from rent_amount.models import RentAmount

# Create your views here.

def send_payment(request,idd):
    obx=RentAmount.objects.get(rent_amount_id=idd)
    context={
        'a':obx
    }

    if request.method=='POST':
        obb=Payment()
        obb.rent_amount_id=idd
        obb.status="paid"
        obb.save()
    return render(request,'payment/send_payment.html',context)

def view_payment_render(request):
    ss= request.session["uid"]
    obx = Payment.objects.filter(rent_amount__distance_tracking__booking_id=ss)
    context = {
        'a': obx
    }
    return render(request,'payment/view_payment_render.html',context)
