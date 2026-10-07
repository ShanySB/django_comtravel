from django.db import models
from django.contrib.auth.models import User
from destinations.models import Destination, Place


# Travel Tips Model 
# Allows users to add travel tip,
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


# Reviews Model 
# Allow Users to write reviws
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


# Cost Info Model 
# Allows User to share cost information
class CostInfo(models.Model):
    CATEGORY_CHOICES = [
        ("food", "Food"),
        ("transport", "Transport"),
        ("accommodation", "Accommodation"),
        ("activities", "Activities"),
        ("other", "Other"),
    ]

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="cost_info"
    )
    destination = models.ForeignKey(
        Destination,
        on_delete=models.CASCADE,
        related_name="cost_info"
    )
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES
    )
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    currency = models.CharField(max_length=3)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.destination} - {self.category} - {self.amount} {self.currency}"


# Question Model 
# Allows User to ask question
class Question(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="questions"
    )
    destination = models.ForeignKey(
        Destination,
        on_delete=models.CASCADE,
        related_name="questions"
    )
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        related_name="questions",
        blank=True,
        null=True
    )
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
