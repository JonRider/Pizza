from django.contrib import admin
from .models import Choice, Topping, Sicilian, Size, Regular, Cart, RegularItem, SicilianItem
# Register your models here.

class CartAdmin(admin.ModelAdmin):
    filter_horizontal = ("regulars", "sicilians")

class RegularAdmin(admin.ModelAdmin):
    filter_horizontal = ("toppings",)

class SicilianItemAdmin(admin.ModelAdmin):
    filter_horizontal = ("toppings",)

admin.site.register(Choice)
admin.site.register(Size)
admin.site.register(Regular)
admin.site.register(Sicilian)
admin.site.register(Topping)
admin.site.register(RegularItem, RegularAdmin)
admin.site.register(SicilianItem, SicilianItemAdmin)
admin.site.register(Cart, CartAdmin)
