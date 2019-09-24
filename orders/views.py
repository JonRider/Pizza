from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.admin.views.decorators import staff_member_required
from decimal import Decimal

from .models import Sicilian, Regular, Pasta, Sub, Salad, Size, Cart, RegularItem, SicilianItem, SubItem, PastaItem, Topping, SubTopping

# Create your views here.
def index(request):
    # Redirect if user is not logged in
    if not request.user.is_authenticated:
        return render(request, "orders/login.html", {"message": None})

    # Disable Place Order Button
    disabled = "disabled"

    # Load saved cart
    try:
        cart = Cart.objects.get(user=request.user, ordered=False)
        disabled = ""
    except Cart.DoesNotExist:
        cart = Cart.objects.create(user=request.user)

    # Calculate Total
    total = Decimal(0)

    for item in cart.regulars.all():
        total += item.regular.price
    for item in cart.sicilians.all():
        total += item.sicilian.price
    for item in cart.subs.filter():
        total += item.sub.price
        # Add sub toppings
        for top in item.toppings.filter():
            total += top.price
    for item in cart.pastas.all():
        total += item.pasta.price
    for item in cart.salads.all():
        total += item.price

    context = {
        "regulars": Regular.objects.all(),
        "sicilians": Sicilian.objects.all(),
        "pastas": Pasta.objects.all(),
        "subs": Sub.objects.all(),
        "salads": Salad.objects.all(),
        "toppings": Topping.objects.all(),
        "sub_toppings": SubTopping.objects.all(),
        "cart_regulars": cart.regulars.all(),
        "cart_sicilians": cart.sicilians.all(),
        "cart_subs": cart.subs.all(),
        "cart_pastas":cart.pastas.all(),
        "cart_salads": cart.salads.all(),
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
    sub_toppings = request.POST.getlist("sub-checks")

    # Disable Place Order Button
    disabled = "disabled"

    # Find users unordered cart or create
    try:
        cart = Cart.objects.get(user=request.user, ordered=False)
        # Enable Buttons if items in cart
        disabled = ""
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

    # Add Sub Item to Cart
    elif type == "sub":
        sub = Sub.objects.get(pk=id)
        sub_item = SubItem.objects.create(sub=sub)
        # add toppings
        for topping in sub_toppings:
            top = SubTopping.objects.get(name=topping)
            sub_item.toppings.add(top)
        # add sub item to cart
        cart.subs.add(sub_item)

    # Add Pasta to Cart
    elif type == "pasta":
        pasta = Pasta.objects.get(pk=id)
        pasta_item = PastaItem.objects.create(pasta=pasta)
        cart.pastas.add(pasta_item)

    # Add Salad to Cart
    elif type == "salad":
        salad = Salad.objects.get(pk=id)
        cart.salads.add(salad)

    # Calculate Total
    total = Decimal(0)
    # Add up cart items
    for item in cart.regulars.all():
        total += item.regular.price
    for item in cart.sicilians.all():
        total += item.sicilian.price
    for item in cart.subs.filter():
        total += item.sub.price
        # Add sub toppings
        for top in item.toppings.filter():
            total += top.price
    for item in cart.pastas.all():
        total += item.pasta.price
    for item in cart.salads.all():
        total += item.price

    context = {
        "regulars": Regular.objects.all(),
        "sicilians": Sicilian.objects.all(),
        "pastas": Pasta.objects.all(),
        "subs": Sub.objects.all(),
        "salads": Salad.objects.all(),
        "toppings": Topping.objects.all(),
        "sub_toppings": SubTopping.objects.all(),
        "cart_regulars": cart.regulars.all(),
        "cart_sicilians": cart.sicilians.all(),
        "cart_subs": cart.subs.all(),
        "cart_pastas": cart.pastas.all(),
        "cart_salads": cart.salads.all(),
        "total": total,
        "disabled": disabled,
        "user": request.user
    }
    return render(request, "orders/index.html", context)

def checkout(request):
    if not request.user.is_authenticated:
        return render(request, "orders/login.html", {"message": None})

    if request.method == "GET":
        # Get the unordered users cart for checkout
        cart = Cart.objects.get(user=request.user, ordered=False)
        cart.ordered = True
        cart.save()
        id = cart.id
        completed = False

    # If user is checking order status
    if request.method == "POST":
        id = int(request.POST["order"])
        order = Cart.objects.get(id=id)
        # if the order has been completed notify user
        if order.completed == True:
            completed = True
        else:
            completed = False

    context = {
        "order": id,
        "completed": completed,
        "user": request.user
    }
    # Display Checkout Page
    return render(request, "orders/order.html", context)

@staff_member_required
def fill(request):
    # If admin is filling an order
    if request.method == "POST":
        # Get the users order number and pull their cart
        id = int(request.POST["order"])
        ordered = Cart.objects.get(id=id)

        # Set order as completed
        ordered.completed = True
        ordered.save()

    # Get Orders that are made but still not completed
    orders = Cart.objects.filter(ordered=True, completed=False)

    context = {
        "orders": orders,
        "user": request.user
    }

    return render(request, "orders/fill.html", context)
