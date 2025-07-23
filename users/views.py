from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView
from django.urls import reverse_lazy
from .models import Address
# Create your views here.
def index(request):
    return render(request, "users/index.html")

class AddressCreateView(CreateView):
    model = Address
    fields = ["title","contact_name", "contact_phone", "province", "city", "district", "place", "email", "is_default"]
    template_name = "users/address_create.html"
    success_url = reverse_lazy('users:addresses')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class AddressUpdateView(UpdateView):
    model = Address
    fields = ["title", "contact_name", "contact_phone", "province", "city", "district", "place", "email", "is_default"]
    template_name = "users/address_update.html"
    success_url = reverse_lazy('users:addresses')

class AddressListView(ListView):
    model = Address
    template_name = "users/address_list.html"
    context_object_name = "addresses"