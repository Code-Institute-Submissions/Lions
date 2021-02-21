from django.shortcuts import render
from .models import Subscription
from .forms import SubscriptionForm

# Create your views here.


def all_subscriptions(request):
    """ A view to show all subscriptions """

    subscriptions = Subscription.objects.all()

    context = {
        "subscriptions": subscriptions
    }

    return render(request, "subscriptions/subscriptions.html", context)


def add_subscription(request):
    """ Add a new subscription to the store """

    form = SubscriptionForm()
    template = "subscriptions/add_subscription.html"
    context = {
        "form":  form
    }

    return render(request, template, context)
