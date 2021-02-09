from django.contrib import admin
from .models import Signup, SignupSubscription
# Register your models here.


class SignupSubscriptionAdminInline(admin.TabularInline):
    def get_max_num(self, request, obj=None, **kwargs):
        max_num = 1

        return max_num
    
    model = SignupSubscription


class SignupAdmin(admin.ModelAdmin):
    inlines = (SignupSubscriptionAdminInline,)

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
