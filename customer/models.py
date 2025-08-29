from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Extend user info if needed:
    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username}"

