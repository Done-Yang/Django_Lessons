from django.shortcuts import render, redirect
from .models import Blog, Student
from django.contrib.auth.models import User
from django.contrib import messages, auth

# Create your views here.
def home(request):
    return render(request, 'generals/index.html')

def deshboard(request):
    new = Blog.objects.all().order_by('-pk')
    student = Student.objects.all().order_by('-pk')

    return render(request, 'deshboards/deshboard.html', {
        'news': new,
        'student': student
    })

def sigUp(request):
    return render(request, 'authentications/signUp.html')

def logIn(request):
    return render(request, 'authentications/logIn.html')

# Systerm's functions
def signUpForm(request):
    userName = request.POST["userName"]
    email = request.POST["email"]
    password = request.POST["password"]
    repassword = request.POST["repassword"]

    if password == repassword:
        if User.objects.filter(username=userName).exists():
            messages.info(request, 'This username is already exist!')
            return redirect('/signUp')
        elif User.objects.filter(email = email).exists():
            messages.info(request, 'This Email is already exist!')
            return redirect('/signUp')
        else:
            user = User.objects.create_user(
                username = userName,
                email = email,
                password = password,
            )
        user.save()
        return redirect('/logIn')   
    else:
        messages.info(request, 'The password do not match!')
        return redirect('/signUp')

def logInForm(request):
    userName = request.POST['username']
    passWord = request.POST['password']

    user = auth.authenticate(username=userName, password=passWord)

    if user is not None:
        auth.login(request, user)
        return redirect('/deshboard')
    else:
        messages.info(request, 'Not found')
        return redirect('/logIn')

def logOut(request):
    auth.logout(request)
    return redirect('/')