from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.urls import reverse
from django.views.decorators.http import require_http_methods
from .forms import LoginForm, RegisterForm


@require_http_methods(["GET", "POST"])
def home(request):
    if request.user.is_authenticated:
        print(dict(request.session.items()))
        print(request.session.get("username"))
        print(request.session.get("email"))
    return render(request, "home/home.html")


@require_http_methods(["GET", "POST"])
def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)

        if not form.is_valid():
            return render(request, "home/login.html", {"form": form})
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, email=username, password=password)
        if user is None:
            form.add_error(None, "用户名或密码错误")
            return render(request, "home/login.html", {"form": form})
        auth_login(request, user)
        return redirect(reverse("home:home"))
    else:
        form = LoginForm()
    return render(request, "home/login.html", {"form": form})


@require_http_methods(["GET", "POST"])
def logout(request):
    auth_logout(request)
    return redirect(reverse("home:home"))


@require_http_methods(["GET", "POST"])
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if not form.is_valid():
            return render(request, "home/register.html", {"form": form})
        user = form.save()
        user.score = 100
        user.save()
        print(reverse("home:login"))
        return redirect(reverse("home:login"))
    else:
        form = RegisterForm()
    return render(request, "home/register.html", {"form": form})
