from django.urls import path
from .views import CreateHireView,UpdateHireStatusView

app_name = 'hire'

urlpatterns = [
    path("create/<int:talent_id>/",CreateHireView.as_view(),name='create-hire'),
    path("status/<int:hire_id>/",UpdateHireStatusView.as_view(), name='update-status')
]