from django.urls import path, re_path
from . import views

app_name = "products"

urlpatterns = [
    path("", views.product_list, name="product_list"),
]
