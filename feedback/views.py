from django.shortcuts import render
from feedback.models import Feedback
from Shop.models import Shop

# Create your views here.

def add_feedback(request):
    ss= request.session["uid"]
    obx = Shop.objects.all()
    context = {
        'b': obx
    }

    if request.method=='POST':
        obb=Feedback()
        obb.user_id=ss
        obb.feedback=request.POST.get('feedback')
        obb.render_id=request.POST.get('shop')
        obb.save()
    return render(request,'feedback/send_feedback.html',context)


def view_feedback_admin(request):
    obb = Feedback.objects.all()
    context = {
        'a': obb
    }
    return render(request,'feedback/view_feedback_admin.html',context)

def view_feedback_public(request):
    obb = Feedback.objects.all()
    context = {
        'a': obb
    }
    return render(request,'feedback/view_feedback_public.html',context)

def view_feedback_render(request):
    ss= request.session["uid"]
    obb = Feedback.objects.filter(render__shop_id=ss)
    context = {
        'a': obb
    }
    return render(request,'feedback/view_feedback_render.html',context)