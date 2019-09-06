from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Sicilian, Regular, Size, Cart, OrderItem, Order, RegularItem, Topping

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
    # Get User order request
    id = int(request.POST["order"])
    type = request.POST["type"]

    # Find users cart or create
    try:
        cart = Cart.objects.get(user=request.user)
    except Cart.DoesNotExist:
        cart = Cart.objects.create(user=request.user)

    # Find Appropriate item in Database and add to cart
    if type == "regular":
        regular = Regular.objects.get(pk=id)
        regular_item = RegularItem.objects.create(regular=regular)
        # add toppings
        toppings = Topping.objects.get(name="Pepperoni")
        regular_item.toppings.add(toppings)
        # add regular item to cart
        cart.regulars.add(regular_item)
    elif type == "sicilian":
        sicilian = Sicilian.objects.get(pk=id)
        cart.sicilians.add(sicilian)


    context = {
        "regulars": Regular.objects.all(),
        "sicilians": Sicilian.objects.all(),
        "cart_regulars": cart.regulars.all(),
        "cart_sicilians": cart.sicilians.all(),
        "user": request.user
    }
    return render(request, "orders/index.html", context)
