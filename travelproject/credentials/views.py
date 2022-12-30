from django.contrib import messages, auth
from django.contrib.auth.models import User

from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method=='POST':
        x=request.POST['username']
        y=request.POST['password']
        user=auth.authenticate(username=x,password=y)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    return render(request,"login.html")
def register(request):
    if request.method== 'POST':
        a=request.POST['username']
        b=request.POST['first_name']
        c=request.POST['last_name']
        d=request.POST['email']
        e=request.POST['password']
        cpassword=request.POST['password1']
        if e==cpassword:
            if User.objects.filter(username=a).exists():
                messages.info(request,"Username Taken")
                return redirect('register')
            elif User.objects.filter(email=d).exists():
                messages.info(request,"Email Taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=a,first_name=b,last_name=c,email=d,password=e)

            user.save();
            return redirect('login')
        else:
            messages.info(request,"password not matching")
            return redirect('register')
        return redirect('/')
    return render(request,"register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')
