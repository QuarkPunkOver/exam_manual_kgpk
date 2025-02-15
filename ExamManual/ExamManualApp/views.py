from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth import logout, update_session_auth_hash
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User as DjangoUser
from ExamManualApp.models import User
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, PasswordResetForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.contrib.auth import authenticate

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['login']
            password = form.cleaned_data['password']
            # поиск пользователя в бд через models User 
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)  # Устанавливаем сессию
                return redirect('home')
            else:
                form.add_error(None, "Неверное имя пользователя или пароль.")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
def home_view(request):
    return render(request, 'home.html')

@login_required
def password_reset_view(request):
    if request.method == 'POST':
        form = PasswordResetForm(user=request.user, data=request.POST)
        if form.is_valid():
            new_password = form.cleaned_data['new_password1']  # Получаем новый пароль
            request.user.password = new_password  # Присваиваем без хэширования
            request.user.FirstAuth = False  # Обновляем статус первичной авторизации
            request.user.save()
            update_session_auth_hash(request, request.user)  # Обновляем сессию
            messages.success(request, "Ваш пароль был успешно обновлен.")
            return redirect('home')
    else:
        form = PasswordResetForm(user=request.user)

    return render(request, 'password_reset_form.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')