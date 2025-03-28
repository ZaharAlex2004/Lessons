from typing import Any

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class CustomUserManager(BaseUserManager):
    """
    Класс CustomUserManager.
    """
    def create_user(self, username: str, email: str, password=None) -> Any:
        """
        Создать польззователя.
        :param username: Имя
        :param email: Эл. почта
        :param password: Пароль
        :return: user
        """
        if not email:
            raise ValueError('Email must be provided')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username: str, email: str, password=None) -> Any:
        """
        Создать администратора.
        :param username: Имя
        :param email: Эл. почта
        :param password: Пароль
        :return: user
        """
        user = self.create_user(username, email, password)
        user.is_admin = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser):
    """
    Класс CustomUser
    """
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username

    def has_perm(self, perm: Any, obj=None) -> Any:
        """
        Имеет перманент.
        :param perm: Any
        :param obj: None
        :return: self.is_admin
        """
        return self.is_admin

    def has_module_perms(self, app_label: Any) -> True:
        """
        Имеет модульные разрешения.
        :param app_label:
        :return:
        """
        return True
