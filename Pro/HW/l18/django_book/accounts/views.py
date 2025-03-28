from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from .forms import UserRegistrationForm, UserLoginForm, MyForm
from .models import CustomUser
from datetime import date


def home_view(request: HttpRequest) -> render:
    """
    Главная страница.
    :param request: HttpRequest
    :return: render
    """
    today = date.today()
    return render(request, 'accounts/home.html', {'today': today})


def submit_view(request: HttpRequest) -> render:
    """
    Рассмотр.
    :param request: HttpRequest
    :return: render
    """
    user_input = None
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            user_input = form.cleaned_data['user_input']
            return render(request, 'accounts/submit.html', {'form': form, 'user_input': user_input})
    else:
        form = MyForm()

    return render(request, 'accounts/submit.html', {'form': form, 'user_input': user_input})


def register_view(request: HttpRequest) -> render:
    """
    Регистрация пользователя.
    :param request: HttpRequest
    :return: render
    """
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']

            user = CustomUser.objects.create(username=username, email=email)
            user.set_password(password)
            user.save()

            login(request, user)

            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})


def user_login_view(request: HttpRequest) -> render:
    """
    Вход пользователя.
    :param request: HttpRequest
    :return: render
    """
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'accounts/login.html', {'form': form})


@login_required
def user_logout_view(request: HttpRequest) -> render:
    """
    Выход пользователя.
    :param request: HttpRequest
    :return: render
    """
    logout(request)
    return redirect('home')


@login_required
def profile_view(request: HttpRequest) -> render:
    """
    Просмотр профиля.
    :param request: HttpRequest
    :return: render
    """
    return render(request, 'accounts/profile.html')
