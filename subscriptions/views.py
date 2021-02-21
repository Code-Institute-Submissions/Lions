from django.shortcuts import render, reverse, redirect, get_object_or_404
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


def edit_subscription(request, subscription_id):
    """ Edit a subscription in the store """
    subscription = get_object_or_404(Subscription, pk=subscription_id)
    if request.method == "POST":
        form = SubscriptionForm(request.POST, request.FILES, instance=subscription)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully updated subscription")
            return redirect(all_subscriptions)
        else:
            messages.error(request, "Failed to update subscription, Please ensure the form is valid.")
    else:
        form = SubscriptionForm(instance=subscription)
        messages.info(request, f"You are editing {subscription.name}")

    template = "subscriptions/edit_subscription.html"
    context = {
        "form":  form,
        "subscription": subscription,
    }

    return render(request, template, context)
