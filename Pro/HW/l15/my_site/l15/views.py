from django.shortcuts import render
from django.http import HttpRequest
from django.utils import timezone


def home_view(request: HttpRequest) -> render:
    """
    Просмотр главной страницы
    :param request: HttpRequest
    :return: render
    """
    today = timezone.now()
    return render(request, "l15/home.html", {"today": today})


def about_view(request: HttpRequest) -> render:
    """
    Просмотр страницы "Про нас"
    :param request: HttpRequest
    :return: render
    """
    return render(request, "l15/about.html")


def contact_view(request: HttpRequest) -> render:
    """
    Просмотр страницы "Контакты"
    :param request: HttpRequest
    :return: render
    """
    return render(request, "l15/contact.html")


def event_view(request: HttpRequest, year=None, month=None, day=None) -> render:
    """
    Просмотр страницы "Событие"
    :param request: HttpRequest
    :param year: Год
    :param month: Месяц
    :param day: День
    :return: render
    """
    return render(request, 'l15/event.html', {'year': year, 'month': month, 'day': day})


def post_view(request: HttpRequest, id: int) -> render:
    """
    Просмотр страницы "Посты"
    :param request: HttpRequest
    :param id: ID
    :return: render
    """
    return render(request, 'l15/post.html', {'id': id})


def profile_view(request: HttpRequest, username: str) -> render:
    """
    Просмотр страницы "Профиль"
    :param request: HttpRequest
    :param username: Имя пользователя
    :return: render
    """
    return render(request, "l15/profile.html", {'username': username})
