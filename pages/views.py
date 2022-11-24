from django.shortcuts import render
from django.http import HttpResponse#ماجد مكتبه بسيطه للشرح في الاغلب لن تحتاجها
# Create your views here.



#دوال بسيطه للشرح
# def index(request):#ماجد
#     return HttpResponse("hello ")#ماجد


def about(request): #كل داله تكتب يجب ربطها بملف الروابط الخاص بالتطبيق وكل داله تمثل صفحه
     return render(request,'pages/about.html')


def header(request):
    
    return render(request,'pages/header.html')
  

    

