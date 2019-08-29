from django.contrib import admin
from .models import Choice, Regular, Topping
# Register your models here.

admin.site.register(Choice)
admin.site.register(Regular)
admin.site.register(Topping)
