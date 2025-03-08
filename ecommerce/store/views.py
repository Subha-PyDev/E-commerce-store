from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            messages.success(request, "Registration successful! Please login.")
            return redirect('login')
        else:
            messages.error(request, "Passwords do not match.")
    
    return render(request, 'store/register.html')

def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('product_list')
        else:
            messages.error(request, "Invalid username or password.")
    
    return render(request, 'store/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')