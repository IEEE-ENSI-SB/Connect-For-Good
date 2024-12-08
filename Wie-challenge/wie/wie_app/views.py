from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.core.files.storage import default_storage
from .models import *
from .forms import InvitationForm

def Donations(request):
    return render(request, 'wie_app/Donations.html', {})

# Login view is no longer needed if you want to remove authentication
def Login_user(request):
    return redirect('feeds')  # Redirect to feeds page or anywhere you want

# Register view can be simplified or removed if not needed
def Register(request):
    return redirect('feeds')  # Redirect to feeds page or anywhere you want

def user_logout(request):
    logout(request)
    return redirect('Donate')

# Removed the @login_required decorator to make the views public
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
            Error = "An error occurred during registration"
    return render(request, 'wie_app/Feeds.html', {'posts': posts, 'add_post': add_post, 'Error': Error})

# Removed the @login_required decorator to make the views public
def Post_view(request, pk):
    post = Invitation.objects.get(id=pk)
    event_participants = post.participants.all()
    count = event_participants.count()
    return render(request, 'wie_app/Post.html', {'post': post, 'count': count})
