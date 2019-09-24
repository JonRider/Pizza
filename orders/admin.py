from django.contrib import admin
from .models import Choice, Topping, Sicilian, Size, Regular, Cart, RegularItem, SicilianItem, Pasta, Sub, SubItem, SubTopping, Salad
# Register your models here.

class CartAdmin(admin.ModelAdmin):
    filter_horizontal = ("regulars", "sicilians", "subs", "salads", "pastas")

class RegularAdmin(admin.ModelAdmin):
    filter_horizontal = ("toppings",)

class SicilianItemAdmin(admin.ModelAdmin):
    filter_horizontal = ("toppings",)

class SubItemAdmin(admin.ModelAdmin):
    filter_horizontal = ("toppings",)

admin.site.register(Choice)
admin.site.register(Size)
admin.site.register(Regular)
admin.site.register(Sicilian)
admin.site.register(Pasta)
admin.site.register(Sub)
admin.site.register(Salad)
admin.site.register(SubTopping)
admin.site.register(SubItem, SubItemAdmin)
admin.site.register(Topping)
admin.site.register(RegularItem, RegularAdmin)
admin.site.register(SicilianItem, SicilianItemAdmin)
admin.site.register(Cart, CartAdmin)
