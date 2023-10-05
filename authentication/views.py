from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def login_page(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request, "Username doesn't exists.")
            return redirect('/login')
            
        user = authenticate(username=username, password=password)
        print("user = ", user)
        if user is None:
            messages.error(request, "Invalid password")
            return redirect('/login')
        else:
            login(request, user)
            return redirect('/')

    return render(request, 'authentication/login.html')

def logout_page(request):
    logout(request)
    return redirect('/login')

def register_page(request):

    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email_id')
        
        user = User.objects.filter(username=username)

        if user.exists():
            messages.info(request, f"{username}, username already exists.")
            return redirect('/register')

        user = User.objects.create(
            first_name = request.POST.get('first_name'),
            last_name = request.POST.get('last_name'),
            username = request.POST.get('username'),
            email=request.POST.get('email_id')
        )

        user.set_password(password)
        user.save()

        return redirect('/register')
    
    return render(request, 'authentication/register.html')