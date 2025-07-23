from django.urls import path
from .views import index, AddressCreateView, AddressListView, AddressUpdateView
app_name = "users"
urlpatterns = [
    path("", index, name="index"),
    path("addresses", AddressListView.as_view(), name="addresses"),
    path("address/create", AddressCreateView.as_view(), name="address_create"),
    path("address/update/<int:pk>", AddressUpdateView.as_view(), name="address_update"),
]