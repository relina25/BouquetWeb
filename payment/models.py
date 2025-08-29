from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Payment(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    paid = models.BooleanField(default=False)
    paid_date = models.DateTimeField(blank=True, null=True)
    payment_method = models.CharField(max_length=50, blank=True)

    def mark_paid(self):
        self.paid = True
        self.paid_date = timezone.now()
        self.save()