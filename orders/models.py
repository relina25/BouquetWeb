from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

ORDER_STATUS_CHOICES = [
    ('created', 'Created'),
    ('shipped', 'Shipped'),
    ('delivered', 'Delivered'),
    ('cancelled', 'Cancelled'),
]

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES, default='created')
    address = models.TextField(blank=True)
    payment_status = models.BooleanField(default=False)

    def __str__(self):
        return f"Order ({self.pk}) by {self.customer.user.username}"

    def total_amount(self):
        return sum(item.sub_total() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price at purchase

    def sub_total(self):
        return self.price * self.quantity

    def __str__(self):
        return f"{self.quantity} of {self.product.name}"
