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


# Review Admin
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "destination",
        "place",
        "rating",
        "created_on",
        "approved",
    )
    list_filter = ("approved", "rating", "destination")
    search_fields = ("title", "body", "author__username")


# Cost Info Admin
@admin.register(CostInfo)
class CostInfoAdmin(admin.ModelAdmin):
    list_display = (
        "author",
        "destination",
        "category",
        "amount",
        "currency",
        "created_on",
    )
    list_filter = ("category", "currency", "destination")
    search_fields = ("description", "author__username")
