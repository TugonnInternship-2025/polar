from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from .models import Skill, Category, UserSkill
from .forms import SkillForm, CategoryForm, UserSkillForm


@login_required
def user_skill_dashboard(request):
    # 1. HANDLE ADDING NEW SKILL (POST)
    if request.method == "POST":
        form = UserSkillForm(request.POST)
        if form.is_valid():
            # Check for duplicates
            already_exists = UserSkill.objects.filter(
                user=request.user, skill=form.cleaned_data["skill"]
            ).exists()

            if already_exists:
                messages.error(request, "You already have this skill added!")
            else:
                user_skill = form.save(commit=False)
                user_skill.user = request.user
                user_skill.save()
                messages.success(request, "Skill added successfully.")
                return redirect("user_skill:user_skill_dashboard")
    # 2. HANDLE LISTING SKILLS (GET)
    else:
        form = UserSkillForm()

    my_skills = UserSkill.objects.filter(user=request.user)
    context = {"form": form, "my_skills": my_skills}

    return render(request, "skills/user_dashboard.html", context)


@login_required
def edit_skill(request, pk):
    """
    Renders a separate small page to edit the skill, then redirects back.
    """
    skill = get_object_or_404(UserSkill, pk=pk, user=request.user)

    if request.method == "POST":
        form = UserSkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            messages.success(request, "Skill updated.")
            return redirect("user_skill:user_skill_dashboard")
    else:
        # GET request: Pre-fill form with existing data
        form = UserSkillForm(instance=skill)

    return render(request, "skills/skill_edit.html", {"form": form})


@login_required
def delete_skill(request, pk):
    skill = get_object_or_404(UserSkill, pk=pk, user=request.user)
    if request.method == "POST":
        skill.delete()
        messages.success(request, "Skill removed.")
    return redirect("user_skill:user_skill_dashboard")


@staff_member_required
def superuser_dashboard(request):
    if request.method == "POST":
        if "add_category" in request.POST:
            c_form = CategoryForm(request.POST)
            if c_form.is_valid():
                c_form.save()
                messages.success(request, "Category Created")
                return redirect("user_skill:superuser_dashboard")

        elif "add_skill" in request.POST:
            s_form = SkillForm(request.POST)
            if s_form.is_valid():
                s_form.save()
                messages.success(request, "Skill Created")
                return redirect("user_skill:superuser_dashboard")

    else:
        c_form = CategoryForm()
        s_form = SkillForm()

    context = {
        "categories": Category.objects.all(),
        "skills": Skill.objects.all(),
        "c_form": c_form,
        "s_form": s_form,
    }
    return render(request, "skills/superuser_dashboard.html", context)
