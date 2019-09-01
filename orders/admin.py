from django.contrib import admin
from .models import Choice, Topping, Sicilian, Size, Regular, Cart
# Register your models here.

admin.site.register(Choice)
admin.site.register(Size)
admin.site.register(Regular)
admin.site.register(Sicilian)
admin.site.register(Topping)
admin.site.register(Cart)
