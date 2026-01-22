from django import forms
from .models import UserSkill, Category, Skill


class UserSkillForm(forms.ModelForm):
    class Meta:
        model = UserSkill
        fields = ["skill", "years_of_experience"]


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name"]


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ["name", "category"]
