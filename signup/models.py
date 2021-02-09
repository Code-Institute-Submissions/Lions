from django.db import models

from subscriptions.models import Subscription
# Create your models here.


class Signup(models.Model):
    subscription_plan = models.ForeignKey(
                                        Subscription, null=True, blank=False,
                                        on_delete=models.SET_NULL)
    price = models.DecimalField(
                                max_digits=10, decimal_places=2,
                                null=False, default=0, editable=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    first_name = models.CharField(max_length=25, null=False, blank=False)
    last_name = models.CharField(max_length=25, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    gender = models.CharField(max_length=10, choices=[
        ("male", "Male"),
        ("female", "Female"),
        ("other", "Other")
    ])
    dob = models.DateField(null=False, blank=False)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self
