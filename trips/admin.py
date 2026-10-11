from django.contrib import admin
from .models import Trip, ItineraryItem


# Trip Admin
@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "user",
        "start_date",
        "end_date",
        "created_on",
    )
    list_filter = ("start_date", "end_date", "created_on")
    search_fields = ("title", "user__username")
