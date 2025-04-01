from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.models import User

def home(request):
    return render(request, 'chat/index.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Check if the user already exists
        if User.objects.filter(username=username).exists():  # Use User model instead of UserProfile
            return JsonResponse({'error': 'Username already taken'}, status=400)

        # Create user with hashed password
        user = User.objects.create_user(username=username, password=password)
        user.save()

        # Automatically log in the user after registration (optional)
        login(request, user)

        return render(request, 'chat/register_success.html')  # ✅ Fixed indentation

    return render(request, 'chat/register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)  # Check user credentials

        if user is not None:
            login(request, user)
            return redirect('http://13.201.132.152:8001/chat/')  # Redirect to the chat page on port 8001 
        else:
            return JsonResponse({'error': 'Invalid credentials'}, status=400)

    return render(request, 'chat/login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def chat_view(request):
    return render(request, "chat/chat.html", {"username": request.user.username})

