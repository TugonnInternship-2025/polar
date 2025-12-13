from django.apps import AppConfig

class UserProfileConfig(AppConfig):
    name = 'user_profile'
    
    # This function loads the signal that creates a user_profile upon a new user creation
    def ready(self):
        import user_profile.signals