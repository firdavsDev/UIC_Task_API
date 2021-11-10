from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages #xabarlar
#Register
def rigester(request):
    if request.method == 'POST':

        form = UserregisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            messages.success(request, f'{username} Akounti yaratildi! Login bo\'lib kirishingiz mumkin!!!')
            return redirect('login')
    else:
        form = UserregisterForm()
    return render(request, 'users/rigester.html',{'form':form})