from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product

# Create your views here.
class ProductListView(ListView):
    model = Product
    paginate_by = 1
    context_object_name = "products"

class ProductDetailView(DetailView):
    model = Product
    context_object_name = "product"

def product_list(request):
    # pass
    products = Product.objects.all()
    return render(request, "products/product_list.html", {"products": products})
