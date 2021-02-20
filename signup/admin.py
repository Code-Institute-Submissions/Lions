from django.contrib import admin
from .models import SubscriptionDetails


class SubscriptionDetailsAdmin(admin.ModelAdmin):

    readonly_fields = (
        "order_number",
        "subscription_price",
        "date"
    )

    fields = (
        "user_profile",
        "full_name",
        "email",
        "phone_number",
        "subscription_type",
        "dob",
        "gender",
    )

    list_display = (
        "order_number",
        "date",
        "user_profile",
        "full_name",
        "subscription_type",
        "subscription_price"
    )

    ordering = ("-date",)

admin.site.register(SubscriptionDetails, SubscriptionDetailsAdmin)
