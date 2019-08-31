from django.db import models

# Create your models here.
class Choice(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"

class Regular(models.Model):
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE) # Number of toppings
    price_small = models.DecimalField(max_digits=5, decimal_places=2)
    price_large = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"regular pizza with {self.choice} topping(s)"

class Sicilian(models.Model):
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE) # Number of toppings
    price_small = models.DecimalField(max_digits=5, decimal_places=2)
    price_large = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"sicilian pizza with {self.choice} topping(s)"


class Topping(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"
