
from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Review(models.Model):
    employer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="given_reviews"
    )
    employee = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="received_reviews"
    )
    comment = models.TextField()
    job_id = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('employer', 'employee')

    def __str__(self):
        return f"{self.employer} reviewed {self.employee}"
