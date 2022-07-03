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
from health.forms import Patientform,Doctorform

# Create your views here.

def FormRender(request):
    #print(request.body)
    context={}
    form=CreateUserForm()
    if request.POST:
        form=CreateUserForm(request.POST)
        
    context={'form': form}
    return render(request,'login.html',context)

def registerPage(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            print("test1")
            return redirect('registration')
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
            if 'next' in request.POST:
                return redirect(request.POST['next'])
            messages.success(request,f'logged in as {user_name}')
            return redirect('home')
        else:
            messages.error(request,f"Invalid Credentials")
            return redirect('login-register')




def user_logout(request):
    context={} 
    logout(request)
    messages.success(request,f"Logout successfull")
    return redirect('home')



def form_view(request):
    context={}
    context={'pform':Patientform(),'dform':Doctorform()}
    return render(request,'pseudo-form.html',context)



def Doctorregister(request):
    if request.method == 'POST':
        form = Doctorform(request.POST)
        if form.is_valid():
            form.save()
            print("test1")
            return HttpResponse('success')
        else:
            return FormRender(request)
    return Http404()




def Patientregister(request):
    if request.method == 'POST':
        form = Patientform(request.POST)
        if form.is_valid():
            form.save()
            print("test1")
            return HttpResponse('success')
        else:
            return FormRender(request)
    return Http404()



