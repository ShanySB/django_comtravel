from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Profile Model
# Stores additional information for each registered user
class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile"
    )

    avatar = CloudinaryField(
        "image",
        blank=True,
        null=True
    )

    bio = models.TextField(
        blank=True
    )

    location = models.CharField(
        max_length=100,
        blank=True
    )

    def __str__(self):
        return f"{self.user.username}'s profile"
