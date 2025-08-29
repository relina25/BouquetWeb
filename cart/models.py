from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Cart ({self.pk}) of {self.customer.user.username}"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def sub_total(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f"{self.quantity} of {self.product.name}"
