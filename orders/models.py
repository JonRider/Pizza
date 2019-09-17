from django.db import models
from django.conf import settings

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
        if self.choice == "Cheese":
            return f"{self.size} regular {self.choice} pizza"
        else:
            return f"{self.size} regular pizza with {self.choice} topping(s)"

class Sicilian(models.Model):
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE) # Number of topping
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        if self.choice == "Cheese":
            return f"{self.size} sicilian {self.choice} pizza"
        else:
            return f"{self.size} sicilian pizza with {self.choice} topping(s)"


class Topping(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class RegularItem(models.Model):
    regular = models.ForeignKey(Regular, on_delete=models.CASCADE)
    toppings = models.ManyToManyField(Topping, blank=True, related_name="toppings")

    def __str__(self):
        if f"{self.regular.choice}" == "Cheese":
            return f"{self.regular.size} regular cheese pizza"
        else:
            add = ""
            list = self.toppings.all()
            add += f"{list[0]}"
            if len(list) > 1:
                add += f", {list[1]}"
            if len(list) > 2:
                add += f" and {list[2]}"
            return f"{self.regular.size} regular pizza with " + add

class SicilianItem(models.Model):
    sicilian = models.ForeignKey(Sicilian, on_delete=models.CASCADE)
    toppings = models.ManyToManyField(Topping, blank=True, related_name="sic_toppings")

    def __str__(self):
        if f"{self.sicilian.choice}" == "Cheese":
            return f"{self.sicilian.size} sicilian cheese pizza"
        else:
            add = ""
            list = self.toppings.all()
            add += f"{list[0]}"
            if len(list) > 1:
                add += f", {list[1]}"
            if len(list) > 2:
                add += f" and {list[2]}"
            return f"{self.sicilian.size} sicilian pizza with " + add

class Cart(models.Model):
    user = models.CharField(max_length=64) # will be propogated with session username
    regulars = models.ManyToManyField(RegularItem, blank=True, related_name="regulars")
    sicilians = models.ManyToManyField(SicilianItem, blank=True, related_name="sicilians")

    def __str__(self):
        return f"{self.user}'s cart. Order #{self.id}"

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
