from django.http import HttpResponse
from django.shortcuts import render
from . models import place
from . models import people
# Create your views here.



def demo(request):
    abc=place.objects.all()
    xyz=people.objects.all()

    return render(request,"index.html",{'result':abc,'players':xyz})
    #return render(request,"index.html",{'players':xyz})
# def addition(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     res=x+y
#     return render(request,"result.html",{'result':res})


