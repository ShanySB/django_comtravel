from django.db import models
from cloudinary.models import CloudinaryField


class Destination(models.Model):
    """
    Respresents a travel destination available on ComTravel
    """
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    country = models.CharField(max_length=100)
    description = models.TextField()
    image = CloudinaryField("image", default="placeholder")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Place(models.Model):
    """
    Respresents a place belonging to a destination
    """
    CATEGORY_CHOICES = [
        ("attraction", "Attraction"),
        ("restaurant", "Restaurant"),
        ("beach", "Beach"),
        ("museum", "Museum"),
        ("landmark", "Landmark"),
        ("shopping", "Shopping"),
        ("entertainment", "Entertainment"),
        ("other", "Other"),
    ]
    destination = models.ForeignKey(
        Destination,
        on_delete=models.CASCADE,
        related_name="places"
    )
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    description = models.TextField()
    image = CloudinaryField("image", default="placeholder")
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["destination", "slug"],
                name="unique_place_slug_per_destination"
            )
        ]

    def __str__(self):
        return self.name
