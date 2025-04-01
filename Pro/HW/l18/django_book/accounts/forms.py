from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.utils import timezone

from .models import CustomUser
from .models import Task


class MyForm(forms.Form):
    """
    Класс MyForm
    """
    user_input = forms.CharField(max_length=100)


class UserRegistrationForm(UserCreationForm):
    """
    Класс UserRegistrationForm
    """
    email = forms.EmailField()

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']


class UserLoginForm(forms.Form):
    """
    Класс UserLoginForm
    """
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self) -> forms:
        """
        Очистка.
        :return: forms
        """
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if user is None:
                raise forms.ValidationError("Invalid login credentials")


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date']

    def clean_due_date(self):
        due_date = self.cleaned_data.get('due_date')
        if due_date and due_date < timezone.now().date():
            raise forms.ValidationError('Дата не может быть в прошлом.')
        return due_date
