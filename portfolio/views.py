from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .models import Represent, Fact,Skill,Resume,Portfolio,Detail
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect


def home(request):
    return render(request, 'portfolio/index.html')
def registerUser(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == "POST":
            email = request.POST.get('email')
            username = request.POST.get('username')
            password = request.POST.get('password')
            password2 = request.POST.get('password2')

            if username and email and password:
                if password == password2:
                    user = User.objects.create(
                        email=email,
                        username=username,
                        password=password,
                    )
                    user.save()
                    login(request, user)
                    return redirect('/')
                else:
                    messages.error(request, "The two password fields didn'/t match.")
                    return HttpResponseRedirect('/register')
            else:
                messages.error(request, "All fields are required.")
                return HttpResponseRedirect('/register')
        return render(request, 'portfolio/register.html')
    
    
def login_user(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            print(request.POST, username, password)
            user = User.objects.get(username=username)
            user = authenticate(  username=username, password=password)
            print(user)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                messages.info(request, 'Username or password is incorrect.')
        return render(request, 'portfolio/login.html')

def logout_user(request):
    logout(request=request)
    return redirect('login')

def represent_user(request):
    represents = Represent.objects.all()
    context = {
        'represents' : represents
    }
    return render(request, 'porfolio/index.html' , context)