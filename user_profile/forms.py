from django.forms import ModelForm
from cloudinary.forms import CloudinaryFileField
from .models import UserProfile


class UserProfileForm(ModelForm):
    image = CloudinaryFileField()

    class Meta:
        model = UserProfile
        fields = ["phone_number", "location", "portfolio_url", "bio", "image"]
