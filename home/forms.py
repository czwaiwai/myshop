from django import forms
from users.models import User

class LoginForm(forms.Form):
    username = forms.EmailField(label="用户名", required=True, max_length=30)
    password = forms.CharField(label="密码", required=True, max_length=30, min_length=6)


class RegisterForm(forms.Form):
    email = forms.EmailField(label="邮箱", required=True, max_length=30)
    mobile = forms.CharField(label="手机号", required=True, max_length=30)
    nickname = forms.CharField(label="昵称", max_length=30)
    password = forms.CharField(label="密码", max_length=30)
    class Meta:
        model = User

