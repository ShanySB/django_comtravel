from django.db import models


class Destination(models.Model):
    """
    Respresents a travel destination available on ComTravel
    """
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    country = models.CharField(max_length=100)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Place(models.Model):
    """
    Respresents a place belonging to a destination
    """
    destination = models.ForeignKey(
        Destination,
        on_delete=models.CASCADE,
        related_name="places"
    )
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
