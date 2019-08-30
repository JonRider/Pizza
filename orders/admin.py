from django.contrib import admin
from .models import Choice, Regular, Topping, Sicilian
# Register your models here.

admin.site.register(Choice)
admin.site.register(Regular)
admin.site.register(Sicilian)
admin.site.register(Topping)
