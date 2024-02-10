from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from cycle.models import Cycle

# Create your views here.

def cycle(request):
    ss= request.session["uid"]
    if request.method=='POST':
        obb=Cycle()
        obb.model=request.POST.get('model')
        obb.type=request.POST.get('type')
        obb.size=request.POST.get('size')
        obb.rent_amount=request.POST.get('amount')
        obb.render_id=ss
        # obb.image=request.POST.get('image')
        myfile = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        obb.image = myfile.name
        obb.save()
    return render(request,'cycle/cycle.html')

def view_cycle_admin(request):
    obb = Cycle.objects.all()
    context = {
        'a': obb
    }
    return render(request,'cycle/view_cycle_admin.html',context)

def view_cycle_public(request):
    obb = Cycle.objects.all()
    context = {
        'b': obb
    }
    return render(request,'cycle/view_cycle_public.html',context)


def view_cycle_user(request):
    obb = Cycle.objects.all()
    context = {
        'b': obb
    }
    return render(request,'cycle/view_cycle_user.html',context)