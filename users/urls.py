from django.urls import path
from .views import index, ClientUserUpdate, AddressCreateView, AddressListView, AddressUpdateView
app_name = "users"
urlpatterns = [
    path("", index, name="index"),
    path("user/<int:pk>/update", ClientUserUpdate.as_view(), name="user_update"),
    path("addresses", AddressListView.as_view(), name="addresses"),
    path("address/create", AddressCreateView.as_view(), name="address_create"),
    path("address/<int:pk>/update", AddressUpdateView.as_view(), name="address_update"),
]