from .models import Ad, Category
from django.db.models import Count
from datetime import timedelta
from django.utils import timezone


def get_ads_last_month():
    """
    Добавление за последнее время.
    :return:
    """
    now = timezone.now()
    return Ad.objects.filter(created_at__gte=now - timedelta(days=30))


def get_active_ads_in_category(category: str):
    """
    Добавление категории.
    :return:
    """
    return Ad.objects.filter(category=category, is_active=True)


def get_ads_with_comment_count():
    """
    Добавление комментария.
    :return:
    """
    return Ad.objects.annotate(comment_count=Count('comment'))


def get_ads_by_user(user: str):
    """
    Добавление пользователя.
    :return:
    """
    return Ad.objects.filter(user=user)
