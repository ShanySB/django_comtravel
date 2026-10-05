from django.contrib import admin
from .models import Destination, Place


@admin.register(Destination)
class Destination(admin.ModelAdmin):
    list_display = ("name", "country", "created_on", "updated_on")
    search_fields = ["name", "country"]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "destination",
        "category",
        "created_on",
        "updated_on",
    )
    list_filter = ("category", "destination")
    search_fields = ["name", "destination_name"]
    prepopulated_fields = {"slug": ("name",)}
