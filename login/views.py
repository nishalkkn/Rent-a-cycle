from django.http import HttpResponseRedirect
from django.shortcuts import render
from login.models import Login

# Create your views here.

def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        passw = request.POST.get("password")
        obj = Login.objects.filter(email=email, password=passw)
        tp = ""
        for ob in obj:
            tp = ob.type
            uid = ob.u_id
            if tp == "admin":
                request.session["uid"] = uid
                return HttpResponseRedirect('/temp/admin/')
            elif tp == "user":
                request.session["uid"] = uid
                return HttpResponseRedirect('/temp/user/')
            elif tp == "shop":
                request.session["uid"] = uid
                return HttpResponseRedirect('/temp/shop/')
        else:
            objlist = "Username or password incorrect... please try angin...!"
            context = {
                'msg': objlist,
            }
            return render(request, 'login/login.html', context)
    return render(request,'login/login.html')
