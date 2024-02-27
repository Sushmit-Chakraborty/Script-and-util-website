from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import SignUpForm,LoginForm
from django.contrib.auth import authenticate,login,logout

# Create your views here.


def registerUser(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('loginUser')
    else:
        form = SignUpForm()

    return render(request,'signup.html',{'form':form})

def loginUser(request):
    try:
        if request.user.is_authenticated:
            return HttpResponse('Success login')
    except:
        print("Error")
    else:
        if request.method == "POST":
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(request,username=username,password=password)
                if user:
                    login(request,user)
                    return redirect('homePage')
        else:
            form = LoginForm()
        return render(request,'login.html',{'form':form})
    

def logoutUser(request):
    logout(request)
    return redirect('loginUser')