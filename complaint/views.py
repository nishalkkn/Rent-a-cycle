from django.shortcuts import render
from complaint.models import Complaint
from Shop.models import Shop

# Create your views here.

def send_complaint(request):
    ss= request.session["uid"]
    obx=Shop.objects.all()
    context={
        'b':obx
    }

    if request.method=='POST':
        obb=Complaint()
        obb.user_id=ss
        obb.complaint=request.POST.get('complaint')
        obb.render_id=request.POST.get('shop')
        obb.reply="pending"
        obb.save()
    return render(request,'complaint/send_complaint.html',context)


def send_reply_render(request,idd):
    if request.method=='POST':
        obb=Complaint.objects.get(complaint_id=idd)
        obb.reply=request.POST.get('reply')
        obb.save()
    return render(request,'complaint/send_reply_render.html')


def view_complaints_admin(request):
    obb=Complaint.objects.all()
    context={
        'a':obb
    }
    return render(request,'complaint/view_complaints_admin.html',context)


def view_complaints_render(request):
    ss= request.session["uid"]
    obb = Complaint.objects.filter(render__shop_id=ss)
    context = {
        'a': obb
    }
    return render(request,'complaint/view_complaints_render.html',context)


def view_reply_user(request):
    ss= request.session["uid"]
    obb = Complaint.objects.filter(user_id=ss)
    context = {
        'a': obb
    }
    return render(request,'complaint/view_reply_user.html',context)