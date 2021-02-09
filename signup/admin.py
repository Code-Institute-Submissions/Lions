from django.contrib import admin
from .models import Signup
# Register your models here.


class SignupAdmin(admin.ModelAdmin):
    readonly_fields = (
        "date",
        "price",
        "dob"
    )

    fields = (
        "email",
        "first_name",
        "last_name",
        "phone_number",
        "gender",
    )

    list_display = (
        "date", "first_name",
        "last_name",
        "price"
    )

    ordering = ("-date",)


admin.site.register(Signup, SignupAdmin)
