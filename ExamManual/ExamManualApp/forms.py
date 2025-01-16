from django import forms

class LoginForm(forms.Form):
    login = forms.CharField(label="Username", max_length=150)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
# форма авторизации пользователя