from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User as DjangoUser
from ExamManualApp.models import User
from django.contrib.auth.decorators import login_required
from .forms import LoginForm

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['login']
            password = form.cleaned_data['password']
            # поиск пользователя в бд через models User 
            user = User.objects.filter(Login=username).first()
            if user and user.Password == password:  # Простое сравнение пароля
                django_user, created = DjangoUser.objects.get_or_create(username=username)
                auth_login(request, django_user)
                return redirect('home')
            else:
                form.add_error(None, "Invalid username or password")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
def home_view(request):
    return render(request, 'home.html')

def logout_view(request):
    logout(request)
    return redirect('login')