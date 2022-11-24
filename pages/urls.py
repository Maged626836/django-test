from django.urls import path#ماجد
from . import views#ماجد

urlpatterns = [#ماجد

    path('index/',views.header,name='index'),#بعد انشاء تطبيق وربط هذا الملف  في ملف الروابط الاساسي ليستطيع المشروع رؤيته قمنا بربط ملف الفيوز الذي بداخله اوامل لتظهر على الشاشه ________ماجد
    path('about/',views.about,name='about'),#ربط الداله الجديده الموجوده في فيوز لتكون مرئيه ويمكن الوصول اليها



]

