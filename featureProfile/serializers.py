from rest_framework import serializers
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = [
            'id',
            'employer',
            'employee',
            'job_id',
            'comment',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['employer', 'created_at', 'updated_at']

