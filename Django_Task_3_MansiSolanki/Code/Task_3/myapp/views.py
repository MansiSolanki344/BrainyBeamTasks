from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            return render(request, 'signup.html', {"error": "User already exists!"})

        User.objects.create_user(username=username, password=password)
        return redirect('login')

    return render(request, 'signup.html')

from django.shortcuts import render
from django.contrib.auth import authenticate, login
from rest_framework_simplejwt.tokens import RefreshToken

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            refresh = RefreshToken.for_user(user)
            return render(request, 'login.html', {
                "message": "Login successful!",
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            })
        else:
            return render(request, 'login.html', {"error": "Invalid credentials!"})

    return render(request, 'login.html')
