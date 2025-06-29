from django import forms


class LoginForm(forms.Form):
    username = forms.EmailField(label="用户名", required=True, max_length=30)
    password = forms.CharField(label="密码", required=True, max_length=30, min_length=6)
