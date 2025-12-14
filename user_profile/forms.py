from django.forms import ModelForm
from .models import UserProfile
# from cloudinary.forms import CloudinaryFileField


class UserProfileForm(ModelForm):
    # image = CloudinaryFileField()

    class Meta:
        model = UserProfile
        fields = ["phone_number", "location", "portfolio_url", "bio", "image"]
