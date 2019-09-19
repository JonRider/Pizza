from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from decimal import Decimal

from .models import Sicilian, Regular, Size, Cart, OrderItem, Order, RegularItem, SicilianItem, Topping

# Create your views here.
def index(request):
    # Redirect if user is not logged in
    if not request.user.is_authenticated:
        return render(request, "orders/login.html", {"message": None})

    # Load saved cart
    try:
        cart = Cart.objects.get(user=request.user)
    except Cart.DoesNotExist:
        cart = Cart.objects.create(user=request.user)

    # Calculate Total
    total = Decimal(0)

    for item in cart.regulars.all():
        total += item.regular.price
    for item in cart.sicilians.all():
        total += item.sicilian.price

    context = {
        "regulars": Regular.objects.all(),
        "sicilians": Sicilian.objects.all(),
        "toppings": Topping.objects.all(),
        "cart_regulars": cart.regulars.all(),
        "cart_sicilians": cart.sicilians.all(),
        "total": total,
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
    topping_list = request.POST.getlist("checks")

    # Find users cart or create
    try:
        cart = Cart.objects.get(user=request.user)
    except Cart.DoesNotExist:
        cart = Cart.objects.create(user=request.user)

    # Find Appropriate item in Database and add to cart
    # Add Regular Item to Cart
    if type == "regular":
        regular = Regular.objects.get(pk=id)
        regular_item = RegularItem.objects.create(regular=regular)
        # add toppings
        for topping in topping_list:
            top = Topping.objects.get(name=topping)
            regular_item.toppings.add(top)
        # add regular item to cart
        cart.regulars.add(regular_item)
    # Add Sicilian Item to Cart
    elif type == "sicilian":
        sicilian = Sicilian.objects.get(pk=id)
        sicilian_item = SicilianItem.objects.create(sicilian=sicilian)
        # add toppings
        for topping in topping_list:
            top = Topping.objects.get(name=topping)
            sicilian_item.toppings.add(top)
        # add sicilian item to cart
        cart.sicilians.add(sicilian_item)

    # Calculate Total
    total = Decimal(0)

    for item in cart.regulars.all():
        total += item.regular.price
    for item in cart.sicilians.all():
        total += item.sicilian.price


    context = {
        "regulars": Regular.objects.all(),
        "sicilians": Sicilian.objects.all(),
        "toppings": Topping.objects.all(),
        "cart_regulars": cart.regulars.all(),
        "cart_sicilians": cart.sicilians.all(),
        "total": total,
        "user": request.user
    }
    return render(request, "orders/index.html", context)

def checkout(request):
    if not request.user.is_authenticated:
        return render(request, "orders/login.html", {"message": None})

    #Display Checkout Page
    return render(request, "orders/order.html")
