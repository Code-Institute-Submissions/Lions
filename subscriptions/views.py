from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Subscription, Category
from .forms import SubscriptionForm, CategoryForm

# Create your views here.


def all_subscriptions(request):
    """ A view to show all subscriptions """

    subscriptions = Subscription.objects.all()

    template = "subscriptions/subscriptions.html"

    context = {
        "subscriptions": subscriptions
    }

    return render(request, template, context)


def all_categories(request):
    """ A view to show all categories """

    if not request.user.is_superuser:
        return redirect(reverse("home"))

    categories = Category.objects.all()

    template = "subscriptions/categories.html"

    context = {
        "categories": categories
    }

    return render(request, template, context)


@login_required
def add_subscription(request):
    """ Add a new subscription to the store """

    if not request.user.is_superuser:
        return redirect(reverse("home"))

    if request.method == "POST":
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(all_subscriptions)

    form = SubscriptionForm()
    template = "subscriptions/add_subscription.html"
    context = {
        "form":  form
    }

    return render(request, template, context)


@login_required
def edit_subscription(request, subscription_id):
    """ Edit a subscription in the store """

    if not request.user.is_superuser:
        return redirect(reverse("home"))

    subscription = get_object_or_404(Subscription, pk=subscription_id)
    if request.method == "POST":
        form = SubscriptionForm(request.POST, request.FILES, instance=subscription)
        if form.is_valid():
            form.save()
            return redirect(all_subscriptions)
    else:
        form = SubscriptionForm(instance=subscription)

    template = "subscriptions/edit_subscription.html"
    context = {
        "form":  form,
        "subscription": subscription,
    }

    return render(request, template, context)


@login_required
def delete_subscription(request, subscription_id):
    """ delete a subscription from the store """

    if not request.user.is_superuser:
        return redirect(reverse("home"))

    subscription = get_object_or_404(Subscription, pk=subscription_id)
    subscription.delete()
    return redirect(all_subscriptions)


@login_required
def add_category(request):
    """ Add a new category to the store """

    if not request.user.is_superuser:
        return redirect(reverse("home"))

    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(all_categories)

    form = CategoryForm()
    template = "subscriptions/add_category.html"
    context = {
        "form":  form
    }

    return render(request, template, context)


@login_required
def edit_category(request, category_id):
    """ Edit a cateogory in the store """

    if not request.user.is_superuser:
        return redirect(reverse("home"))

    category = get_object_or_404(Category, pk=category_id)
    if request.method == "POST":
        form = CategoryForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            form.save()
            return redirect(all_categories)
    else:
        form = CategoryForm(instance=category)

    template = "subscriptions/edit_category.html"
    context = {
        "form":  form,
        "category": category,
    }

    return render(request, template, context)


@login_required
def delete_category(request, category_id):
    """ delete a category from the store """

    if not request.user.is_superuser:
        return redirect(reverse("home"))

    category = get_object_or_404(Category, pk=category_id)
    category.delete()
    return redirect(all_categories)
