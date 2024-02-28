from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from App.models import Active, CustomUser

# Create your views here.
@login_required(login_url='/')
def hod(request):
    return render(request, 'hod.html')

def signUp(request):
    return render(request, 'signUp.html')

def logIn(request):
    return render(request, 'logIn.html')

def deshboard(request):
    return render(request, 'index.html')

# Authenrications
def addUser(request):
    user_name = request.POST['username']
    email = request.POST['email']
    password = request.POST['psw']
    re_password = request.POST['repsw']

    if password==re_password:
        if CustomUser.objects.filter(username=user_name).exists():
            messages.info(request, 'This user name is exists!')
            return redirect('/signUp')
        elif CustomUser.objects.filter(email=email).exists():
            messages.info(request, 'This email is exists!')
            return redirect('/signUp')
        else:
            user = CustomUser.objects.create_user(
                username=user_name,
                email=email,
                password=password,
                user_type = 2,
            )
            user.save()
            return redirect('/')

    else:
        messages.info(request, 'The password is not match!')
        return redirect('/signUp')

# def sigUpForm(request):
    user_name = request.POST['username']
    email = request.POST['email']
    password = request.POST['psw']
    re_password = request.POST['repsw']

    if password==re_password:
        if CustomUser.objects.filter(username=user_name).exists():
            messages.info(request, 'This user name is exists!')
            return redirect('/signUp')
        elif CustomUser.objects.filter(email=email).exists():
            messages.info(request, 'This email is exists!')
            return redirect('/signUp')
        else:
            user = CustomUser.objects.create_user(
                username=user_name,
                email=email,
                password=password,
                user_type = 2,
            )
            user.save()
            return redirect('/')

    else:
        messages.info(request, 'The password is not match!')
        return redirect('/signUp')

def logInForm(request):
    username = request.POST['username']
    password = request.POST['psw']

    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        if user.user_type == '1':
            return redirect('/hod')
        if user.user_type == '2':
            return redirect('/deshboard')              
       
    else:
        messages.info(request, 'You must sign up first')
        return redirect('/')

def logOut(request):
    auth.logout(request)
    return redirect('/')
