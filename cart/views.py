import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from cart.models import Cart, CartItem
from cart.forms import AddCartForm
from products.models import ProductSKU


# Create your views here.
@login_required(login_url=reverse_lazy("home:login"))
@require_http_methods(["GET", "POST"])
def index(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    return render(request, "cart/index.html", {"cart": cart})

@login_required(login_url=reverse_lazy("home:login"))
@require_http_methods(["POST"])
def add(request):
  form = AddCartForm(request.POST)
  if not form.is_valid():
     return JsonResponse({"success": False, "msg":"表单未验证未通过", "errors": json.dumps(form.errors.as_json())})
  cart, created = Cart.objects.get_or_create(user=request.user)
  sku_id = form.cleaned_data.get("sku_id")
  quantity = form.cleaned_data.get("quantity")
  sku =  ProductSKU.objects.get(pk=sku_id)
  try:
      cart_item = CartItem.objects.get(cart=cart, product=sku)
      cart_item.quantity = cart_item.quantity + quantity
      cart_item.save()
  except CartItem.DoesNotExist:
      cart_item = CartItem.objects.create(cart=cart, sku=sku, quantity=quantity)
  return JsonResponse({"success": True, "cart_item": cart_item})
