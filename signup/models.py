import uuid

from django.db import models

from subscriptions.models import Subscription
from profiles.models import UserProfile
# Create your models here.


class SubscriptionDetails(models.Model):
    class Meta:
        verbose_name_plural = "Subscription details"

    Choices = [
        ("male", "Male"),
        ("female", "Female"),
        ("other", "Other")
    ]

    order_number = models.CharField(max_length=32, null=False, blank=False, editable=False)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name="subscriptions")
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    gender = models.CharField(max_length=10, choices=Choices)
    date = models.DateTimeField(auto_now_add=True)
    dob = models.DateField(null=False, blank=False)
    subscription_type = models.ForeignKey(Subscription, null=False, blank=True, on_delete=models.CASCADE)
    subscription_price = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False)

    # from https://github.com/ckz8780/boutique_ado_v1/blob/faaa31bcbd1bcc5fdf7d54c57d51c031df9d7460/checkout/models.py
    def _generate_order_number(self):
        """ Generate random, unique string using UUID """
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()

        self.subscription_price = self.subscription_type.price

        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number
