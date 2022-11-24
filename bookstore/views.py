from django.shortcuts import render
from .models import books
# Create your views here.


def bookstoremain(request):
    x = {"pooksobject":books.objects.all()}

    return render(request,'bookstore/bookstoremain.html',x)