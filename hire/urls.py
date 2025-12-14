from django.urls import path
from .views import CreateHireView

app_name = 'hire'

urlpatterns = [
    path("create/<int:talent_id>/",CreateHireView.as_view(),name='create-hire') 
]