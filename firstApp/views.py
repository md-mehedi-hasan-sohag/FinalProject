from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout



# Create your views here.
def home(request):
    return render(request, 'firstApp/index.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse('User logged in successfully')
        if '@' in username:
            user = User.objects.filter(email=username).first()
            if user is not None:
                username = user.username
        if user is not None:
            login(request, user)
            return HttpResponse('User logged in successfully')
        return render(request, 'firstApp/signin.html', {'error': 'Invalid credentials'})
    return render(request, 'firstApp/signin.html')

def signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm-password')

        if User.objects.filter(email=email).exists():
            return render(request, 'firstApp/signup.html', {'error': 'Email already exists'})
        
        if User.objects.filter(username=username).exists():
            return render(request, 'firstApp/signup.html', {'error': 'Username already exists'})

        if password != confirm_password:
            return render(request, 'firstApp/signup.html', {'error': 'Passwords do not match'})
        
        new_user = User.objects.create_user(username=username, email=email, password=password)

        if new_user is None:
            return render(request, 'firstApp/signup.html', {'error': 'Error creating user'})
        
        new_user.first_name = firstname
        new_user.last_name = lastname
        new_user.save()

        return render(request, 'firstApp/signin.html')

    return render(request, 'firstApp/signup.html')