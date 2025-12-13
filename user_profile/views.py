from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm
from .models import UserProfile


def new_profile(request):
    """
    This won't be needed as a signal can be setup to trigger a profile creation upon new user signup
    """
    pass


@login_required
def view_profile(request):
    """
    This endpoint displays user's profile. The frontend can access data using example syntax below:
      <h1>{{ profile.user.username }}'s Profile</h1>
      <p>Bio: {{ profile.bio }}</p>
    """

    # We are only fetching the profile tied to the person currently logged in, an nothing else, even if someone tries to snoop around.
    profile = get_object_or_404(UserProfile, user=request.user)
    context = {"profile": profile}

    return render(request, "profile_view.html", context)


@login_required
def edit_profile(request):
    """
    This endpoint updates user profile data. It first shows a form prefilled with user profile data, then upon submit, it makes relevant changes to the profile record.
    """

    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == "POST":
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("user_profile:view_profile")
    else:
        form = UserProfileForm(instance=profile)

    context = {"profile": profile, "form": form}

    return render(request, "profile_edit.html", context)
