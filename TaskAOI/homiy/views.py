from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import Homiy
from .forms import ArizaForm
# Create your views here.

@login_required 
def addAriza(request):
    user = request.user
    
    homiy=Homiy.objects.all().order_by('-pk').filter(user=request.user)

    form=ArizaForm()

    if request.method=='POST':
        form=ArizaForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
        return redirect('sendAdmin')

    context={'homiy':homiy,'form':form}
    return render(request,'homiy.html',context)
