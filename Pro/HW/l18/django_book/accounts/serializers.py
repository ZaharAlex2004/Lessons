from django.utils import timezone
from rest_framework import serializers
from .models import Task, User


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date']

    def validate_due_date(self, value):
        if value and value < timezone.now().date():
            raise serializers.ValidationError('Дата не може бути у минулому.')
        return value


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']


class TaskWithUserSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'user']

    def validate_due_date(self, value):
        if value and value < timezone.now().date():
            raise serializers.ValidationError('Дата не може бути у минулому.')
        return value
