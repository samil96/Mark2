from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.
def home(request):
    template = 'index.html'
    return render(request, template)
    
"""
def registration(request):    
    if request.method == 'POST':
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid():           
            formulario.save()
            return redirect('login')
        else:                               
            messages.add_message(request, messages.INFO, formulario.errors)           
            return redirect('registro')
    else:
        formulario = UserCreationForm()
    return render(request, 'registration/registro.html', {'formulario':formulario})
"""
