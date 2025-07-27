from django import forms
from .models import CartItem

class AddCartForm(forms.Form):
    sku_id = forms.CharField(required=True)
    quantity = forms.IntegerField(required=True, min_value=1)


