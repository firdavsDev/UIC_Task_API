from django.db import models
from django.contrib.auth.models import User 


# Create your models here.
class Homiy(models.Model):
    
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    # student = models.ForeignKey('Student',on_delete=models.CASCADE,blank=True,null=True)
    
    shaxs = models.CharField(max_length=50)
    fish = models.CharField(max_length=100)
    phone = models.CharField(max_length=25)
    price = models.IntegerField()
    group_name = models.CharField(max_length=255)
    
    def __str__(self):
        return f'{self.fish}: {self.shaxs}'
    
    class Meta:
        verbose_name_plural = "Homiylar"
    