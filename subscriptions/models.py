from django.db import models
import datetime

# Create your models here.


class Category(models.Model):

    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254)
    # stores duration of subscription
    duration = models.DurationField()

    def __str__(self):
        return self.name


class Subscription(models.Model):

    name = models.CharField(max_length=254)
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name
