from django import forms
from django.contrib.auth.forms import SetPasswordForm
class LoginForm(forms.Form):

    login = forms.CharField(label="Username", max_length=150)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
# форма авторизации пользователя

class PasswordResetForm(SetPasswordForm):
    class Meta:
        fields = ['new_password1', 'new_password2']

    new_password1 = forms.CharField(
        label="Новый пароль",
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
    )
    new_password2 = forms.CharField(
        label="Подтвердите пароль",
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
    )
#Форма сброса пароля