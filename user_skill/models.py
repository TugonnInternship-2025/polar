from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categories"  # To correct 'Categorys' in Django Admin

    def __str__(self):
        return self.name


class Skill(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class UserSkill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)

    years_of_experience = models.PositiveIntegerField(help_text="Years of experience")

    class Meta:
        # Makes sure a user cannot add the same skill twice
        unique_together = ("user", "skill")

    def __str__(self):
        return f"{self.user.username} - {self.skill.name}"