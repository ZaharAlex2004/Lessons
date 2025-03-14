from django.shortcuts import render
from django.http import HttpRequest
from django.utils import timezone
from django.views import View


class ContactView(View):
    """
    Класс ContactView
    """
    def get(self, request: HttpRequest) -> render:
        """
        Просмотр страницы "Контакты"
        :param request: HttpRequest
        :return: render
        """
        return render(request, "main/contact_bl.html")


class ServiceView(View):
    """
    Класс ServiceView
    """
    def get(self, request: HttpRequest) -> render:
        """
        Просмотр страницы "Услуги"
        :param request: HttpRequest
        :return: render
        """
        services = [
            {"name": "Веб-розробка", "description": "Розробка сайтів", "price": 500},
            {"name": "SEO-оптимізація", "description": "Оптимізація для пошукових систем", "price": 300},
            {"name": "Маркетинг", "description": "Просування в інтернеті", "price": 200},
        ]
        return render(request, "main/service_bl.html", {'services': services})


def home_view(request: HttpRequest) -> render:
    """
    Просмотр главной страницы
    :param request: HttpRequest
    :return: render
    """
    today = timezone.now()
    return render(request, "main/home.html", {"today": today})


def about_view(request: HttpRequest) -> render:
    """
    Просмотр страницы "Про нас"
    :param request: HttpRequest
    :return: render
    """
    return render(request, "main/about_bl.html")


def event_view(request: HttpRequest, year=None, month=None, day=None) -> render:
    """
    Просмотр страницы "Событие"
    :param request: HttpRequest
    :param year: Год
    :param month: Месяц
    :param day: День
    :return: render
    """
    return render(request, 'main/event.html', {'year': year, 'month': month, 'day': day})


def post_view(request: HttpRequest, id: int) -> render:
    """
    Просмотр страницы "Посты"
    :param request: HttpRequest
    :param id: ID
    :return: render
    """
    return render(request, 'main/post.html', {'id': id})


def profile_view(request: HttpRequest, username: str) -> render:
    """
    Просмотр страницы "Профиль"
    :param request: HttpRequest
    :param username: Имя пользователя
    :return: render
    """
    return render(request, "main/profile.html", {'username': username})
