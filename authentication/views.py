from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
User = get_user_model()

# Create your views here.
def login_page(request):

    if request.method == "POST":
        email_id = request.POST.get('email_id')
        password = request.POST.get('password')

        if not User.objects.filter(email=email_id).exists():
            messages.error(request, "Email id doesn't exists.")
            return redirect('/login')
            
        user = authenticate(request, username=email_id, password=password)
        # user = authenticate(request, email_id, password)
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