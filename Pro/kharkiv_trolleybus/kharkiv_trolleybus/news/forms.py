from django import forms
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm
from django.core.exceptions import ValidationError

from .models import *


def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(f"{value} isn`t an even number")

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']  # Только поле контента
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Введите ваш комментарий...'}),
        }

class NewsForm(forms.ModelForm):
    title = forms.CharField(label= 'Название: ', max_length=255, widget=forms.TextInput())
    sourse = forms.CharField(label= 'Источник: ', max_length=255, widget=forms.TextInput())
    date_published = forms.DateField(label= 'Дата: ')
    content = forms.Textarea(attrs={'rows': 4, 'placeholder': 'Описание: '})
    class Meta:
        model = News
        fields = ['title', 'sourse', 'date_published', 'content']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-styling'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-styling'}))

    class Meta:
        model = User
        fields = ['username', 'password1']

class RegistrationForm(UserCreationForm):
    username = forms.CharField(label= 'Имя пользователя', max_length=255, widget=forms.TextInput(attrs={'class': 'form-styling'}))
    email = forms.EmailField(label= 'Эл. почта', max_length=255, widget=forms.EmailInput(attrs={'class': 'form-styling'}))
    password1 = forms.CharField(label= 'Пароль', widget=forms.PasswordInput(attrs={'class': 'form-styling'}))
    password2 = forms.CharField(label= 'Подтвердить пароль', widget=forms.PasswordInput(attrs={'class': 'form-styling'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError("Пользователь з таким email уже существует!")
        return email


class CustomPasswordChangeForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']

class UserLoginForm(forms.Form):
    username = forms.CharField(label= 'Имя пользователя', max_length=100, widget=forms.TextInput(attrs={'class': 'form-styling'}))
    password = forms.CharField(label= 'Пароль',widget=forms.PasswordInput(attrs={'class': 'form-styling'}))

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadFiles
        fields = ['file']

class UploadVideoForm(forms.ModelForm):
    class Meta:
        model = UploadVideoFile
        fields = ['file', 'title']

class PhotoGalleryForm(forms.ModelForm):
    class Meta:
        model = PhotoGallery
        fields = ['title', 'image', 'description']
