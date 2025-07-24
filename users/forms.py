from django import forms
from .models import ClientUser

class ClientUserUpdateForm(forms.ModelForm):
    class Meta:
        model = ClientUser
        fields = ['username', 'avator', 'nickname', 'email', 'mobile']
        # widgets = {
        #     'score': forms.NumberInput(attrs={'type': 'number'}),
        # }
