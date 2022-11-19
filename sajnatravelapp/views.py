from django.http import HttpResponse
from django.shortcuts import render
from . models import dest,news
# Create your views here.
def fun(request):
    obj=dest.objects.all()
    obj1 = news.objects.all()
    return render(request,'index.html',{'results':obj,'results1':obj1})
# def fun1(request):
#     obj1=news.objects.all()
#     return render(request,'index.html',{'results1':obj1})

# def addition(request):
#     numb1 = int(request.POST["num1"])
#     numb2 = int(request.POST["num2"])
#     numb3 = numb1 + numb2
#     return render(request,"result.html",{'add':numb3})