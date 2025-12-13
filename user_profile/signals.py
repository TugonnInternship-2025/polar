from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import UserProfile


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Creates a UserProfile automatically when a new User is created.
    """

    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """
    Updates the UserProfile whenever the User is saved.
    This ensures that if the User object is saved, the linked Profile is also saved, keeping them in sync.
    """

    instance.userprofile.save()
