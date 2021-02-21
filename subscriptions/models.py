from django.db import models

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

    def get_friendly_name(self):
        return self.friendly_name


class Subscription(models.Model):

    name = models.CharField(max_length=254)
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    sku = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name
