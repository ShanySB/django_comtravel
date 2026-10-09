from django.db import models
from django.contrib.auth.models import User
from destinations.models import Place


# Trip Model
# Allows users to create and manage their own trips
class Trip(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="trips"
    )
    title = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# Itinerary Item Model
# Allows users to add activities and plan their trips
class ItineraryItem(models.Model):
    trip = models.ForeignKey(
        Trip,
        on_delete=models.CASCADE,
        related_name="itinerary_items"
    )
    place = models.ForeignKey(
        Place,
        on_delete=models.SET_NULL,
        related_name="itinerary_items",
        blank=True,
        null=True
    )
    date = models.DateField()
    time = models.TimeField(blank=True, null=True)
    notes = models.TextField(blank=True)
    cost_estimate = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )
    link = models.URLField(blank=True)

    def __str__(self):
        return f"{self.trip.title} - {self.date}"
