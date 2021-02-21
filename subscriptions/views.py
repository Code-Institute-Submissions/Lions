from django.shortcuts import render, reverse, redirect
from django.contrib import messages
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

    if request.method == "POST":
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully added subscription")
            return redirect(reverse("add_subscription"))
        else:
            messages.error(request, "Failed to add subscriprion. Please double check the details.")

    form = SubscriptionForm()
    template = "subscriptions/add_subscription.html"
    context = {
        "form":  form
    }

    return render(request, template, context)
