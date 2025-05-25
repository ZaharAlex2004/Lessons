from celery import shared_task
from django.core.mail import send_mail
from django.contrib.auth.models import User
import logging

logger = logging.getLogger(__name__)

@shared_task
def send_registration_email(email):
    try:
        user = User.objects.get(email=email)
        send_mail(
            'Харьковский троллейбус',
            f'Благодарим вас за регистрацию! Добро пожаловать {user.username}',
            'noreply@example.com',
            [user.email],
            fail_silently=False,
        )
    except User.DoesNotExist:
        logger.error(f"User with email {email} does not exist.")

@shared_task
def send_promotional_email(email):
    try:
        user = User.objects.get(email=email)
        send_mail(
            'Наши возможности',
            'Создавайте статью по новостям и добавляйте видео, фото!',
            'noreply@example.com',
            [user.email],
            fail_silently=False,
        )
    except User.DoesNotExist:
        logger.error(f"User with email {email} does not exist.")

@shared_task
def log_user_count():
    user_count = User.objects.count()
    print(f"Пользоватей в БД: {user_count}")
