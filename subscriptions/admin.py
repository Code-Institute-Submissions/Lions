from django.contrib import admin
from .models import Subscription, Category

# Register your models here.


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "category",
        "price",
    )


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "duration",
    )


admin.site.register(Subscription, SubscriptionAdmin)
admin.site.register(Category, CategoryAdmin)
