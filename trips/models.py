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
created_on = models.DateTimeField(auto_now=True)


def __str__(self):
    return f"{self.title}"


# Itinerary Item Model
# Allows users to add activities and plan their trips
class ItineraryItem(models.Model):
    trip = models.ForeignKey(
        Trip,
        on_delete=models.CASCADE,
        related_name="itinerary_items"
    )
