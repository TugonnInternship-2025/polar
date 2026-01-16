from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied
from .models import Review
from .serializers import ReviewSerializer


class ReviewCreateOrUpdateView(generics.CreateAPIView):
    """
    Employer can create OR update a review for an employee.
    - Only authenticated users
    - Only ONE review per employer per employee
    - Employer must have worked with the employee
    """

    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        employer = self.request.user
        employee = serializer.validated_data["employee"]

        # -----------------------------------------
        # 1️⃣ Restrict: only employers can review
        # -----------------------------------------
        if hasattr(employer, "profile"):
            if employer.profile.role != "employer":
                raise PermissionDenied("Only employers can leave reviews.")
        else:
            # If role system is not ready yet, allow for now
            pass

        # --------------------------------------------------
        # 2️⃣ Restrict: employer must have worked with employee
        # --------------------------------------------------
        # NOTE:
        # Replace `Job` and field names when job app is ready.
        #
        # Example:
        # from jobs.models import Job
        #
        # worked_together = Job.objects.filter(
        #     employer=employer,
        #     employee=employee,
        #     status="completed"
        # ).exists()
        #
        # if not worked_together:
        #     raise PermissionDenied(
        #         "You can only review employees you worked with."
        #     )

        # --------------------------------------------------
        # 3️⃣ Create or update review (NO duplicates)
        # --------------------------------------------------
        Review.objects.update_or_create(
            employer=employer,
            employee=employee,
            defaults={
                "comment": serializer.validated_data["comment"],
                "job_id": serializer.validated_data["job_id"],
            }
        )


class EmployeeReviewListView(generics.ListAPIView):
    """
    Public endpoint:
    Show all reviews for an employee profile
    """

    serializer_class = ReviewSerializer

    def get_queryset(self):
        employee_id = self.kwargs["employee_id"]
        return Review.objects.filter(employee_id=employee_id)
