from django.shortcuts import render
from .models import Subscription

# Create your views here.


def all_subscriptions(request):
    """ A view to show all subscriptions """

    subscriptions = Subscription.objects.all()

    context = {
        "subscriptions": subscriptions
    }

    return render(request, "subscriptions/subscriptions.html", context)