from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from .models import CustomUser


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
