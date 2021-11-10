from django.db import models
from homiy.models import Homiy
# Create your models here.

class TalabaHomiy(models.Model):
    ajratilgan_suma = models.IntegerField()
    homiy = models.ForeignKey(Homiy,on_delete=models.SET_NULL,blank=True,null=True)
    student = models.ForeignKey('Student',on_delete=models.SET_NULL,blank=True,null=True)

    def __str__(self):
        return f'{self.homiy} homiylik - {self.student}'

    class Meta:
        verbose_name_plural = "Talabalar_Homiylari"
        db_table = 'Talaba_Homiy'


class Student(models.Model):
    fish = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    OTM = models.CharField(max_length=50) # Smart select paketidan  foydalansak ham buladi bunda
    type = models.CharField(max_length=50) # choise dan ham foydalansak bular edi
    contract_price = models.IntegerField()
    talaba_hommiyi = models.ForeignKey(Homiy,on_delete=models.SET_NULL,null=True,blank=True)
    # created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.fish
    
    class Meta:
        verbose_name_plural = "Studentlar"
        # db_table = 'Talaba'
