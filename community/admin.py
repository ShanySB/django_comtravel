from django.contrib import admin
from .models import TravelTip, Review, CostInfo, Question, Answer


# Travel Tip Admin
@admin.register(TravelTip)
class TravelTipAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "destination",
        "place",
        "created_on",
        "approved",
    )
    list_filter = ("approved", "destination", "created_on")
    search_fields = ("title", "body", "author_username")
