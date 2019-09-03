from django.db import models
from django.conf import settings
# Choices
PIZZA_CHOICES = (
    ('R', 'Regular'),
    ('S', 'Sicilian')
)

SIZE_CHOICES = (
    ('S', 'Small'),
    ('L', 'Large')
)

# Create your models here.
class Choice(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class Size(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class Regular(models.Model):
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE) # Number of toppings
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.size} regular pizza with {self.choice} topping(s)"

class Sicilian(models.Model):
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE) # Number of topping
    price_small = models.DecimalField(max_digits=5, decimal_places=2)
    price_large = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"sicilian pizza with {self.choice} topping(s)"


class Topping(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.CharField(max_length=64) # will be propogated with session username
    regulars = models.ManyToManyField(Regular, blank=True, related_name="regulars")
    sicilians = models.ManyToManyField(Sicilian, blank=True, related_name="sicilians")

class OrderItem(models.Model):
    item = models.ForeignKey(Regular, on_delete=models.CASCADE)

    def __str__(self):
        return self.item

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
