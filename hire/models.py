from django.db import models
from django.contrib.auth.models import User


class HireModel(models.Model):
    STATUS_PENDING = 'pending'
    STATUS_COMPLETED = 'completed'
    STATUS_CANCELLED = 'cancelled'
    
    STATUS_CHOICES = [
        (STATUS_PENDING, 'Pending'),
        (STATUS_COMPLETED, 'Completed'),
        (STATUS_CANCELLED, 'Cancelled'),
    ]
    
    ALLOWED_TRANSITIONS = {
        STATUS_PENDING: [STATUS_COMPLETED, STATUS_CANCELLED],
        STATUS_COMPLETED: [],
        STATUS_CANCELLED: [],
    }
    
    client = models.ForeignKey(User,on_delete=models.CASCADE, related_name='hires_made')
    talent = models.ForeignKey(User,on_delete=models.CASCADE, related_name='hires_gotten')
    talent_name = models.CharField(max_length=255)
    talent_location = models.CharField(max_length=255,blank=True)
    talent_contact = models.CharField(max_length=255,blank=True)
    talent_email = models.EmailField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_PENDING)
    hired_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True,blank=True)
    
    def can_transition_to(self,new_status):
        return new_status in self.ALLOWED_TRANSITIONS[self.status]
    
    def __str__(self):
        return f"Hire {self.id} - {self.talent_name} - ({self.status})"
    