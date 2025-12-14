from django.urls import path
from . import views

app_name = "user_profile"

urlpatterns = [
    path("", views.view_profile, name="view_profile"),
    path("/edit", views.edit_profile, name="edit_profile"),
    # No need for new profile URL, as django signal can quickly setup a new profile upon user creation
    # path("new/", views.new_profile, name="new_profile"),
]
