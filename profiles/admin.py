from django.contrib import admin
from .models import Profile


# Profile Admin
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "location")
    search_fields = ("user_username", "location")
