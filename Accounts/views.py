from ast import Return
from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm 
from .forms import CreateUserForm
from django.http import HttpResponse,Http404
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
# Create your views here.

def FormRender(request):
    #print(request.body)
    context={}
    form=CreateUserForm()
    if request.POST:
        print("you")
        form=CreateUserForm(request.POST)
        
    context={'form': form}
    return render(request,'login.html',context)

def registerPage(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            print("test1")
            return HttpResponse('success')
        else:
            return FormRender(request)
    return Http404()


def loginpage(request):
    if request.POST:
        user_name=request.POST["username"]
        pass_word=request.POST["password"]
        user=authenticate(request,username=user_name,password=pass_word)
        if user is not None:
            login(request,user)
            return HttpResponse(f'logged in as {user_name}')
        else:
            messages.error(request,f"Invalid Credentials")
            return redirect('login-register')



def user_logout(request):
    context={} 
    return HttpResponse("Logout successfull")

