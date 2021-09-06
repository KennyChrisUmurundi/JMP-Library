from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm as BaseAuthenticationForm
from django.contrib.auth.forms import PasswordResetForm as BasePasswordResetForm
from django.contrib.auth.forms import SetPasswordForm as BaseSetPasswordForm
from django.contrib.auth.forms import UsernameField
from django.contrib.auth import password_validation


class loginForm(forms.Form):

    username = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                "name": "username",
                "class": "woocommerce-Input woocommerce-Input--text input-text form-control",
                "type": "text",
                "placeholder": "Username",
                "id": "username",
            }
        ),
    )

    password = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                "name": "password",
                "class": "woocommerce-Input woocommerce-Input--text input-text form-control",
                "type": "password",
                "placeholder": "password",
                "id": "password",
            }
        ),
    )


class UserRegisterForm(UserCreationForm):

    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                "name": "username",
                "class": "form-control",
                "type": "text",
                "placeholder": "Your mail",
            }
        )
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
