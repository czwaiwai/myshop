from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from cart.models import Cart


# Create your views here.
@require_http_methods(["GET", "POST"])
def index(request):
    return render(request, "cart/index.html")
    # cart_items = Cart.objects.filter(user=request.user)
