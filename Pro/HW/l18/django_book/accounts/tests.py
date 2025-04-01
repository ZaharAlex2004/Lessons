import os
import random
import string
import time
import uuid

import django
import pytest
from django.contrib.auth import get_user_model
from django.utils import timezone
from rest_framework.exceptions import ValidationError
from .forms import TaskForm
from .models import Task, User
from .serializers import TaskSerializer, TaskWithUserSerializer


@pytest.mark.django_db
def test_task_form_valid_data():
    form_data = {
        'title': 'Test Task',
        'description': 'This is a test task.',
        'due_date': timezone.now().date() + timezone.timedelta(days=1),
    }
    form = TaskForm(data=form_data)
    assert form.is_valid()


@pytest.mark.django_db
def test_task_form_missing_required_fields():
    form_data = {
        'title': '',
        'description': '',
        'due_date': '',
    }
    form = TaskForm(data=form_data)
    assert not form.is_valid()
    assert 'title' in form.errors
    assert 'description' in form.errors
    assert 'due_date' in form.errors


@pytest.mark.django_db
def test_task_form_invalid_due_date():
    form_data = {
        'title': 'Test Task',
        'description': 'This is a test task.',
        'due_date': timezone.now().date() - timezone.timedelta(days=1),
    }
    form = TaskForm(data=form_data)
    assert not form.is_valid()
    assert 'due_date' in form.errors


@pytest.mark.django_db
def test_task_serializer_valid_data():
    task_data = {
        'title': 'Test Task',
        'description': 'This is a test task.',
        'due_date': timezone.now().date() + timezone.timedelta(days=1),
    }
    serializer = TaskSerializer(data=task_data)
    assert serializer.is_valid()


@pytest.mark.django_db
def test_task_serializer_missing_required_fields():
    task_data = {
        'title': '',
        'description': '',
        'due_date': '',
    }
    serializer = TaskSerializer(data=task_data)
    assert not serializer.is_valid()
    assert 'title' in serializer.errors
    assert 'description' in serializer.errors
    assert 'due_date' in serializer.errors


@pytest.mark.django_db
def test_task_serializer_invalid_due_date():
    task_data = {
        'title': 'Test Task',
        'description': 'This is a test task.',
        'due_date': timezone.now().date() - timezone.timedelta(days=1),
    }
    serializer = TaskSerializer(data=task_data)
    with pytest.raises(ValidationError):
        serializer.is_valid(raise_exception=True)


import pytest
from django.contrib.auth import get_user_model


@pytest.fixture
def user():
    username = f'testuser_{uuid.uuid4().hex[:8]}'
    email = f'{username}@example.com'
    return get_user_model().objects.create(username=username, email=email)


@pytest.mark.django_db
def test_task_with_user_serializer_valid_data():
    username = f'testuser_{uuid.uuid4().hex[:8]}_{random.randint(10000, 99999)}'
    email = f'{username}@example.com'

    # Создаем нового пользователя с уникальными данными
    user = get_user_model().objects.create(username=username, email=email)

    task_data = {
        'title': 'Test Task',
        'description': 'This is a test task.',
        'due_date': timezone.now().date() + timezone.timedelta(days=1),
        'user': {
            'username': user.username,
            'email': user.email,
        }
    }

    serializer = TaskWithUserSerializer(data=task_data)
    assert serializer.is_valid(), f"Errors: {serializer.errors}"


@pytest.mark.django_db
def test_task_with_user_serializer_invalid_user_data():
    task_data = {
        'title': 'Test Task',
        'description': 'This is a test task.',
        'due_date': timezone.now().date() + timezone.timedelta(days=1),
        'user': {
            'username': '',
            'email': 'invalidemail',
        }
    }
    serializer = TaskWithUserSerializer(data=task_data)
    assert not serializer.is_valid()
    assert 'user' in serializer.errors
    assert 'username' in serializer.errors['user']
    assert 'email' in serializer.errors['user']


@pytest.fixture(autouse=True)
def clear_db():
    from django.core.management import call_command
    call_command('flush', '--no-input', verbosity=0)
