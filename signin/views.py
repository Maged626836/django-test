from django.shortcuts import render
from .models import users

# Create your views here.





def signin(request): #كل داله تكتب يجب ربطها بملف الروابط الخاص بالتطبيق وكل داله تمثل صفحه
     username = request.POST.get('username')
     password = request.POST.get('password')
     print(username)
     data = users(username = username,password = password)
     data.save()
     return render(request,'Subscription/signin.html')



