from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Sicilian, Regular, Size, Cart

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return render(request, "orders/login.html", {"message": None})
    context = {
        "regulars": Regular.objects.all(),
        "sicilians": Sicilian.objects.all(),
        "user": request.user
    }
    return render(request, "orders/index.html", context)

def register(request):
    if request.method == "GET":
        return render(request, "orders/register.html", {"message": None})
    else:
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is None:
            user = User.objects.create_user(username, email, password)
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "orders/register.html", {"message": "User already exists."})

def login_view(request):
    if request.method == "GET":
        return render(request, "orders/login.html", {"message": None})
    else:
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "orders/login.html", {"message": "Invalid credentials."})

def logout_view(request):
    logout(request)
    return render(request, "orders/login.html", {"message": "Logged out."})

def order(request):
    if not request.user.is_authenticated:
        return render(request, "orders/login.html", {"message": None})
    regular_id = int(request.POST["order"])
    regular = Regular.objects.get(pk=regular_id)
    cart = Cart.objects.get(user="Jon")
    cart.regulars.add(regular)
    regulars_list = list(Cart.objects.filter(user="Jon"))
    context = {
        "regulars": Regular.objects.all(),
        "sicilians": Sicilian.objects.all(),
        "ordered": regular,
        "regulars_list": regulars_list,
        "user": request.user
    }
    return render(request, "orders/index.html", context)
