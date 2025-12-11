from django.forms import ModelForm     
from cloudinary.forms import CloudinaryFileField
from .models import UserProfile

class UserProfileForm(ModelForm):
    image = CloudinaryFileField()

    class Meta:
        model = UserProfile
        fields = ['image', 'bio', 'location', 'phone_number', 'portfolio_url']
