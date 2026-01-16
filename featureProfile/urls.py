from django.urls import path
from .views import ReviewCreateOrUpdateView, EmployeeReviewListView

urlpatterns = [
    path('reviews/', ReviewCreateOrUpdateView.as_view(), name='review-create'),
    path(
        'employees/<int:employee_id>/reviews/',
        EmployeeReviewListView.as_view(),
        name='employee-reviews'
    ),
]
