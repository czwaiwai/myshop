import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict
from utils.decorators import login_required_json
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


@login_required_json
@require_http_methods(["POST"])
def add(request):
    # 得到一个前端提交的form表单
    print(request.POST)
    form = AddCartForm(request.POST)
    if not form.is_valid():
        print(form.errors.as_json())
        return JsonResponse(
            {
                "success": False,
                "msg": "表单未验证未通过",
                "errors": json.loads(form.errors.as_json()),
            }
        )
    # 读取form表单中的数据
    sku_id = form.cleaned_data.get("sku_id")
    quantity = form.cleaned_data.get("quantity")
    # 如果用户不存在购物车则自动创建一个购物车
    cart, created = Cart.objects.get_or_create(user=request.user)

    # 查询当前产品的sku对象
    sku = None
    try:
        # python没有块级作用域，所以sku是可以直接在后面使用的
        sku = ProductSKU.objects.get(pk=sku_id)
    except ProductSKU.DoesNotExist:
        return JsonResponse({"success": False, "msg": "产品不存在"})
    try:
        # 查询当前sku产品是否在购物车中
        cart_item = CartItem.objects.get(cart=cart, sku=sku)
        # 存在则将产品的数量进行累加
        cart_item.quantity = cart_item.quantity + quantity
        cart_item.save()
    except CartItem.DoesNotExist:
        # 不存在则将创建一个CartItem对象
        cart_item = CartItem.objects.create(cart=cart, sku=sku, quantity=quantity)
    return JsonResponse({"success": True, "cart_item": model_to_dict(cart_item)})
