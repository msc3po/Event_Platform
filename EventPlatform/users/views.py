from django.shortcuts import render, redirect
from django.urls import path
from .models import User
from .forms import UserSettingsForm

# Create your views here.
def user_account_settings(request):
    
    if request.method == "POST":
        form = UserSettingsForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()

            return redirect('user_account_settings') 
        
    else:
        form = UserSettingsForm(instance=request.user)
    context = {'form': form}
    return render(request, 'users/templates/users/account_settings.html', context)
    
    
    
    context={}
    return render (request, 'users/account_settings.html', context)