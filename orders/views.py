from django.http import HttpResponse
from django.shortcuts import render

from .models import Regular, Sicilian

# Create your views here.
def index(request):
    context = {
        "regulars": Regular.objects.all(),
        "sicilians": Sicilian.objects.all(),
    }
    return render(request, "orders/index.html", context)
