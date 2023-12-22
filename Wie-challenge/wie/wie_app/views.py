from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.core.files.storage import default_storage
from .models import *
from .forms import InvitationForm


def Donations(request):
    return render(request, 'wie_app/Donations.html', {})

def Login_user(request):
    if request.user.is_authenticated:
        return redirect('feeds')
    page = 'LOGIN'
    if request.method == 'POST':
        Email = request.POST.get('Email').lower()
        password = request.POST.get('password')
        user = authenticate(request , email = Email, password = password)
        if user is not None:
            login(request, user)
            return redirect('feeds')
    return render(request, 'wie_app/Auth.html', {'page' : page})

def Register(request):
    if request.user.is_authenticated:
        return redirect('feeds')
    if request.method == 'POST':
        image = request.FILES['image']
        file_name = default_storage.save(image.name, image)
        username = request.POST.get('username')
        name = username
        password =make_password(request.POST.get('password1'))
        email = request.POST.get('Email').lower()
        phone = request.POST.get('phone')
        user = CustomUser.objects.create(image=file_name, name=name, username=username, password=password, email=email, phone=phone)
        user.save()
        return redirect('feeds')
    return render(request, 'wie_app/Auth.html', {})

def user_logout(request):
    logout(request)
    return redirect('Donate')

@login_required(login_url='login')
def Feeds(request):
    Error = ""
    posts = Invitation.objects.all().order_by('-date')
    add_post = InvitationForm()
    if request.method == 'POST':
        add_post = InvitationForm(request.POST)
        if add_post.is_valid():
            add_post.save()
            return redirect('feeds')
        else:
            Error = "An error occured during registration"
    return render(request, 'wie_app/Feeds.html', {'posts': posts, 'add_post':add_post, 'Error':Error})


@login_required(login_url='login')
def Post_view(request, pk):
    post = Invitation.objects.get(id=pk)
    event_participants = post.participants.all()
    count = event_participants.count()
    return render(request, 'wie_app/Post.html', {'post': post, 'count': count})
