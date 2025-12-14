from django.urls import path
from .views import home

app_name = 'hire'

urlpatterns = [
    path("",home) 
]