from multiprocessing import context
from django.conf import PASSWORD_RESET_TIMEOUT_DAYS_DEPRECATED_MSG
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def hi(request):
    return render(request,'sandy/index.html')
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            return redirect('userpage')
        elif username=='admin' and password=='admin@nov07':
            return redirect('welcomepage')
        else:
            messages.error(request,'Invalid username and password')
        
    context = {}    
    return render(request,'sandy/login.html', context)
def register(request):
    form = CreateUserForm()
    
    
    if request.method ==  "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account was created successfully')
            return redirect('loginpage')
    context = {'form':form}
    return render(request,'sandy/register.html',context)
def contact(request):
    return render(request,'sandy/contact.html')
def welcome(request):
    return render(request,'sandy/welcome.html')
def bill(request):
    return render(request,'sandy/billing.html')
def user(request):
    return render(request,'sandy/userwelcome.html')
def makeorder(request):
    return render(request,'sandy/makeorder.html')
def about(request):
    return render(request,'sandy/about.html')
def status(request):
    return render(request,'sandy/status.html') 
def userprofile(request):
    return render(request,'sandy/userprofile.html')
def adminprofile(request):
    return render(request,'sandy/adminprofile.html')

