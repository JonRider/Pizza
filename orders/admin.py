from django.contrib import admin
from .models import Choice, Topping, Sicilian, Size, Regular, Cart, Pasta, Sub, SubTopping, Salad, Dinner
# Register your models here.

class CartAdmin(admin.ModelAdmin):
    filter_horizontal = ("regulars", "sicilians", "subs", "salads", "pastas", "dinners")

admin.site.register(Choice)
admin.site.register(Size)
admin.site.register(Regular)
admin.site.register(Sicilian)
admin.site.register(Pasta)
admin.site.register(Sub)
admin.site.register(Salad)
admin.site.register(Dinner)
admin.site.register(SubTopping)
admin.site.register(Topping)
admin.site.register(Cart, CartAdmin)
