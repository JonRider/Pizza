from django.http import HttpResponse
from django.shortcuts import render

from .models import Sicilian, Regular, Size

# Create your views here.
def index(request):
    context = {
        "regulars": Regular.objects.all(),
        "sicilians": Sicilian.objects.all(),
    }
    return render(request, "orders/index.html", context)

def order(request):
    regular_id = int(request.POST["order"])
    regular = Regular.objects.get(pk=regular_id)
    context = {
        "regulars": Regular.objects.all(),
        "sicilians": Sicilian.objects.all(),
        "ordered": regular,
    }
    return render(request, "orders/index.html", context)
