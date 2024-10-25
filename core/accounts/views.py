from django.shortcuts import render

from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm



def login_view(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            username=request.POST['username']
            password=request.POST['password']
            user = authenticate(request,username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect('/')
        return render(request,'accounts/login.html')
    else:
        return redirect('/')

def register_view(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            form =UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
        form=UserCreationForm()
        context={'form':form}
        return render (request,'accounts/register.html',context)
    else:
        return redirect('/')

@login_required
def logout_view(request):
    logout(request)
    return redirect('/')
