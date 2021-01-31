from django.contrib import admin
from .models import Slideshow

# Register your models here.


class HomeAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "text",
        "image",
    )


admin.site.register(Slideshow, HomeAdmin)
