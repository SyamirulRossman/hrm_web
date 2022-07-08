from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.
from django.http import HttpResponse


def home(request):
    return render(request, 'index.html')


def log_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            first_name = user.first_name
            messages.success(request, "Logged In Sucessfully!!")
            return render(request, "dashboard.html", {"first_name": first_name})
        else:
            messages.error(request, "Wrong Credentials!!")
            return redirect('log_in')

    return render(request, 'log_in.html')


def log_out(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('home')

