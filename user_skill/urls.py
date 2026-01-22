from django.urls import path
from . import views

app_name = "user_skill"

urlpatterns = [
    path("dashboard/", views.user_skill_dashboard, name="user_skill_dashboard"),
    path("superuser/", views.superuser_dashboard, name="superuser_dashboard"),
    path("edit/<int:pk>/", views.edit_skill, name="edit_skill"),
    path("delete/<int:pk>/", views.delete_skill, name="delete_skill"),
]
