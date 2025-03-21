import logging
from typing import Any

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import Ad, User


logger = logging.getLogger(__name__)


@receiver(post_save, sender=Ad)
def send_new_ad_email(sender: Any, instance: Any, created: Any, **kwargs: dict[str, Any]) -> None:
    """
    Отправление новым пользователем.
    :param sender: Отправитель
    :param instance: Пример
    :param created: Создано
    :param kwargs: Ключевые аргументы
    :return:
    """
    if created:
        send_mail(
            'Нове оголощення',
            f'Ви створили нове оголощення: {instance.title}',
            "zaharalex04@gmail.com",
            [instance.user.email],
            settings.DEFAULT_FROM_EMAIL,
        )


@receiver(post_save, sender=Ad)
def deactivate_ad_after_30_days(sender: Any, instance: Any, **kwargs: dict[str, Any]) -> None:
    """
    Деактивация после 30 дней.
    :param sender: Отправитель
    :param instance: Пример
    :param kwargs: Ключевые аргументы
    :return:
    """
    instance.deactivate_after_30_days()
