from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Subscription

# Create your views here.


def all_subscriptions(request):
    """ A view to show all subscriptions """

    subscriptions = Subscription.objects.all()

    context = {
        "subscriptions": subscriptions
    }

    return render(request, "subscriptions/subscriptions.html", context)


@login_required
def subscription_signup(request, sub_id):
    """ A view to allow users to signup for gym subscriptions """

    sub = get_object_or_404(Subscription, pk=sub_id)

    context = {
        "subscription": sub
    }

    return render(request, "subscriptions/subscription_signup.html", context)
