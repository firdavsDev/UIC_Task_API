from django.forms import fields

from django import forms
from django.contrib.auth.models import User
from .models import Homiy
#models
#ruyhatdan utish
class ArizaForm(forms.ModelForm):
    class Meta:
        model = Homiy
        fields = ['shaxs','fish','phone','price','group_name',]


