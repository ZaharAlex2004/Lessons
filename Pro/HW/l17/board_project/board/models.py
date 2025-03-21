from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import timedelta


class User(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.username


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class Ad(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def deactivate_after_30_days(self):
        """
        Метод для автоматической деактивации объявления через 30 дней
        :return:
        """
        if timezone.now() > self.created_at + timedelta(days=30):
            self.is_active = False
            self.save()

    def clean(self):
        """
        Валидатор для поля цены, проверка на положительное значение
        :return:
        """
        if self.price <= 0:
            raise ValidationError('Ціна має бути позитивним числом.')


class Comment(models.Model):
    content = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    ad = models.ForeignKey(Ad, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey('User', on_delete=models.CASCADE)

    def __str__(self):
        return f'Коментарій {self.user} до оголошення {self.ad}'

    @staticmethod
    def count_comments(ad):
        """
        Метод для подсчета комментариев к объявлению
        :param ad: Объявление
        :return:
        """
        return ad.comments.count()
