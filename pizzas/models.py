from django.db import models

class Pizza(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_vegetarian = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Pizza"
        verbose_name_plural = "Pizzas"

class Topping(models.Model):
    name = models.CharField(max_length=50)
    pizza = models.ForeignKey(Pizza, related_name='toppings', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Topping"
        verbose_name_plural = "Toppings"
        
