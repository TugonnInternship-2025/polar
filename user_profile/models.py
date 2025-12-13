from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = CloudinaryField("image", null=True, blank=True)
    bio = models.TextField(null=True, blank=True)  # Optional
    location = models.CharField(max_length=50, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    portfolio_url = models.CharField(max_length=100, null=True, blank=True)  # Optional
