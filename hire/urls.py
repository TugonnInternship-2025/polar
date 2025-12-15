from django.urls import path
from .views import CreateHireView,UpdateHireStatusView,GetHireListView,GetHireView

app_name = 'hire'

urlpatterns = [
    path("create/<int:talent_id>/",CreateHireView.as_view(),name='create-hire'),
    path("status/<int:hire_id>/",UpdateHireStatusView.as_view(), name='update-status'),
    path("all/<int:user_id>/",GetHireListView.as_view(), name = "get-all-hires"),
    path("<int:hire_id>/", GetHireView.as_view(), name = "get-hire-by-id")
]