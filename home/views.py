from django.shortcuts import render
from .forms import LoginForm


# Create your views here.
def home(request):
    return render(request, "home/home.html")


def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            return render(request, "home/home.html")
    else:
        form = LoginForm()
    return render(request, "home/login.html", {"form": form})


def register(request):
    pass
