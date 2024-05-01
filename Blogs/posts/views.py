from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Posts

# Create your views here.


def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username already exists')
                return redirect('register.html')
            else:
                user = User.objects.create_user(username=username, password=password2)
                user.save()
                return redirect('login.html')
        else:
            messages.info(request, 'password does not match')
            return redirect('register.html')
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('blogspost.html')
        else:
            messages.info(request, "User Does Not Exist")
            return redirect('login.html')
    else:
        return render(request, 'login.html')


def blogspost(request):
    blogsposts = Posts.objects.all()
    return render(request, 'blogspost.html', {'blogsposts': blogsposts})


def posts(request, pk):
    blogsposts = Posts.objects.get(id=pk)
    return render(request, 'posts.html', {'blogsposts': blogsposts})
