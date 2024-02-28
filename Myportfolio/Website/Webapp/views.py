from django.shortcuts import render, redirect
from .models import Experian, Profile, Skill, Comment
from . import models
from django.shortcuts import get_object_or_404
from .form import AddSheet

# Create your views here.
def home(request):
    experains = Experian.objects.all()
    profile = Profile.objects.all()
    skill = Skill.objects.all()
    comment = Comment.objects.all()
    cm = comment[:4]

    if request.method == 'POST':
        form = AddSheet(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddSheet

    context = {
        'experains': experains,
        'form': form,
        'profile':profile,
        'skills':skill,
        'comment':cm,
    }

    return render(request, 'index.html', context)

def sendcomment(request):
    if request.method == 'POST':
        cm = models.Comment(
            comment=request.POST['message'], 
        )
        cm.save()
        return redirect('home')