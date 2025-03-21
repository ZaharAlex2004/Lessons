from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404
from datetime import timedelta
from django.utils import timezone
from .models import Ad, User, Comment
from .services import *


def home_view(request: HttpRequest) -> render:
    """
    Просмотр главной страницы
    :param request: HttpRequest
    :return: render
    """
    today = timezone.now()
    return render(request, "board/board.html", {"today": today})


def ad_list_view(request):
    """
    Список объявлений с фильтрацией по категории, статусу и пользователю.
    :param request:
    :return:
    """
    # Получаем все категории и пользователей для отображения в фильтре
    categories = Category.objects.all()
    users = User.objects.all()

    # Начальный запрос на все объявления
    ads = Ad.objects.all()

    # Фильтрация по категории
    if 'category' in request.GET and request.GET['category']:
        ads = ads.filter(category_id=request.GET['category'])

    # Фильтрация по статусу (активные/неактивные)
    if 'status' in request.GET and request.GET['status']:
        if request.GET['status'] == 'active':
            ads = ads.filter(is_active=True)
        elif request.GET['status'] == 'inactive':
            ads = ads.filter(is_active=False)

    # Фильтрация по пользователю
    if 'user' in request.GET and request.GET['user']:
        ads = ads.filter(user_id=request.GET['user'])

    # Аннотируем количество комментариев для каждого объявления
    ads = ads.annotate(comment_count=Count('comments'))

    # Отправляем данные в шаблон для отображения
    return render(request, 'board/ads_list.html', {
        'ads': ads,
        'categories': categories,
        'users': users,
    })


def ad_detail_view(request: HttpRequest, ad_id: int):
    ad = get_object_or_404(Ad, id=ad_id)
    comments = ad.comments.all()  # Все комментарии для текущего объявления

    if request.method == 'POST':
        text = request.POST.get('comment')
        if text:
            Comment.objects.create(ad=ad, user=request.user, content=text)

    return render(request, 'board/ads_list.html', {
        'ad': ad,
        'comments': comments,
    })
