from django.db import models
from datetime import datetime
# Create your models here.



class books(models.Model):
    x =[      #الليستات 
        ('horror','horror'),#الاسم الاول هو اللي هيتحفظ في الاكواد والتاني اللى هيظهر للادمن في الصفحه 
        ('action','action'),
        ('comedy','comedy'),
        ('effects and ambiguity','effects and ambiguity'),
        ('drama','drama'),
        
    
    
    
    ]
    nameofbook = models.CharField(max_length=10)
    content = models.TextField(null=True,blank=True,verbose_name = 'a description')#البلانك والنول دايما مع بعض
    price = models.DecimalField(max_digits=5,decimal_places=2)
    images = models.ImageField(upload_to='photosfolder/%y/%m/%d',default='photosfolder/22/11/22/pexels1.jpg')
    available =models.BooleanField(default=True)
    category = models.CharField(max_length=30,null=True,blank=True,choices=x) #خاصية تشويسس بتعمل قائمه منسدله واديتها اسم الليستهاللي هتاخدها
    Production_Date = models.DateField(default=datetime.now)#from datetime import datetimeلاعمل قيمه افتراضيه بالتاريخ الحالي والوقت يجب استدعاء مكتبة دات تيم
    Auto_post_time = models.TimeField(default=datetime.now)#from datetime import datetimeلاعمل قيمه افتراضيه بالتاريخ الحالي والوقت يجب استدعاء مكتبة دات تيم
    posting_time = models.DateTimeField(default=datetime.now)#from datetime import datetimeلاعمل قيمه افتراضيه بالتاريخ الحالي والوقت يجب استدعاء مكتبة دات تيم




    class Meta:
        verbose_name = 'my books'

    def __str__(self):
		      return self.nameofbook

    

    

