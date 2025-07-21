from django.urls import path, re_path
from .views import ProductListView,ProductDetailView, product_list

app_name = "products"

urlpatterns = [
    # path("", product_list, name="product_list"),
    path('', ProductListView.as_view(), name="product_list"),
    path('<int:pk>', ProductDetailView.as_view(), name="product_detail"),
]
