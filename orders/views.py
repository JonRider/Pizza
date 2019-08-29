from django.http import HttpResponse
from django.shortcuts import render

from .models import Regular, Choice, Topping

# Create your views here.
def index(request):
    context = {
        "regulars": Regular.objects.all(),
    }
    return render(request, "orders/index.html", context)
