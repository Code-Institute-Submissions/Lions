from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserProfile
from .forms import UserProfileForm

from signup.models import SubscriptionDetails

# Create your views here.


@login_required
def profile(request):
    """ Display user's profile """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully")
        else:
            messages.error(request, "Failed to update profile, please ensure the form is valid.")

    subscriptions = profile.subscriptions.all()
    form = UserProfileForm(instance=profile)

    template = "profiles/profile.html"
    context = {
        "form": form,
        "subscriptions": subscriptions,
    }

    return render(request, template, context)
