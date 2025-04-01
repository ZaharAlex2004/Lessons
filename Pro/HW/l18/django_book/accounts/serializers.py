from typing import Any

from django.utils import timezone
from rest_framework import serializers
from .models import Task, User


class TaskSerializer(serializers.ModelSerializer):
    """
    Класс TaskSerializer
    """
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date']

    def validate_due_date(self, value: {__lt__}) -> Any:
        """
        Проверка срока оплаты
        :param value: Цель
        :return: value
        """
        if value and value < timezone.now().date():
            raise serializers.ValidationError('Дата не може бути у минулому.')
        return value


class UserSerializer(serializers.ModelSerializer):
    """
    Класс UserSerializer
    """
    class Meta:
        model = User
        fields = ['username', 'email']


class TaskWithUserSerializer(serializers.ModelSerializer):
    """
    Класс TaskWithUserSerializer
    """
    user = UserSerializer()

    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'user']

    def validate_due_date(self, value: {__lt__}) -> Any:
        """
        Проверка срока оплаты
        :param value: Цель
        :return: value
        """
        if value and value < timezone.now().date():
            raise serializers.ValidationError('Дата не може бути у минулому.')
        return value
