from django.db import models
from django.contrib.auth.models import User
from destinations.models import Destination, Place


class TravelTip(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="travel_tips"
    )
    destination = models.ForeignKey(
        Destination,
        on_delete=models.CASCADE,
        related_name="travel_tips"
    )
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        related_name="travel_tips",
        blank=True,
        null=True
    )
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Review(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="reviews"
    )
    destination = models.ForeignKey(
        Destination,
        on_delete=models.CASCADE,
        related_name="reviews"
    )
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        related_name="reviews",
        blank=True,
        null=True
    )
    rating = models.IntegerField(
        choices=[(i, i) for i in range(1, 6)]
    )
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.title
