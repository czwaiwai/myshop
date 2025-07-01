from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import User


class LoginForm(forms.Form):
    username = forms.EmailField(label="用户名", required=True, max_length=30)
    password = forms.CharField(label="密码", required=True, max_length=30, min_length=6)


class RegisterForm(UserCreationForm):
    username = forms.CharField(label="用户名", required=True, max_length=30)
    email = forms.EmailField(label="邮箱", required=True, max_length=30)
    mobile = forms.CharField(label="手机号", required=True, max_length=30)
    nickname = forms.CharField(label="昵称", required=False, max_length=30)
    # password = forms.CharField(label="密码", max_length=30)

    class Meta:
        model = User
        fields = ["email", "password1", "password2", "username", "mobile", "nickname"]
