from django.urls import path#ماجد
from . import views#ماجد

urlpatterns = [#ماجد

    path('',views.bookstoremain,name='bookstore'),
]

