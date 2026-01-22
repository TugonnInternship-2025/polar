from django.contrib import admin
from .models import Category, Skill, UserSkill

admin.site.register(Category)
admin.site.register(Skill)
admin.site.register(UserSkill)
