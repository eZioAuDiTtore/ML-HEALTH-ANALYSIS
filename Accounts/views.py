from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm 
from .forms import CreateUserForm
# Create your views here.

def registerPage(request):
    form=CreateUserForm()
    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
    context={'form': form}
    return render(request,'login.html',context)

def loginpage(request):
    context={}
    return render(request,'Acoounts/login.html',context)

def user_logout(request):
    context={}
    return HttpResponse("Logout successfull")

