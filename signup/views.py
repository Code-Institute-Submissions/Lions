from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required

from .models import SubscriptionDetails
from subscriptions.models import Subscription

from .forms import SignupForm

from profiles.forms import UserProfileForm
from profiles.models import UserProfile

import stripe


@login_required
def signup(request, sub_id):

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():

            form_data = {
                "full_name": request.POST["full_name"],
                "email": request.POST["email"],
                "phone_number": request.POST["phone_number"],
                "dob": request.POST["dob"],
                "gender": request.POST["gender"],
                "subscription_type": sub_id,
            }

            signup_form = SignupForm(form_data)

        if signup_form.is_valid():
            signup = signup_form.save()

            request.session["save_info"] = "save-info" in request.POST
            return redirect(reverse("payment_success", args=[signup.order_number]))
        else:
            return redirect("signup", sub_id=sub_id)

    if request.user.is_authenticated:
        try:
            profile = UserProfile.objects.get(user=request.user)
            signup_form = SignupForm(initial={
                "full_name": profile.user.get_full_name(),
                "email": profile.user.email,
                "phone_number": profile.default_phone_number,
                "dob": profile.default_dob,
                "gender": profile.default_gender,
            })
        except UserProfile.DoesNotExist:
            signup_form = SignupForm()
    else:
        signup_form = SignupForm()

    subscription_type = get_object_or_404(Subscription, id=sub_id)
    subscription_price = subscription_type.price
    stripe_total = round(subscription_price * 100)

    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    template = "signup/signup.html"

    context = {
        "stripe_public_key": stripe_public_key,
        "client_secret": intent.client_secret,
        "signup_form": signup_form,
        "price": subscription_price,
        "sub_id": sub_id
    }

    return render(request, template, context)


@login_required
def payment_success(request, order_number):
    """
    Handle successful checkouts
    """
    save_info = request.session.get("save_info")
    order = get_object_or_404(SubscriptionDetails, order_number=order_number)

    # from https://github.com/ckz8780/boutique_ado_v1/blob/be009dd6c8db8c9cbc18aa5b8dd8a04daa194ed0/checkout/views.py#L143
    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        # Attach the user's profile to the order
        order.user_profile = profile
        order.save()

    if save_info:
        profile_data = {
            "default_email": order.email,
            "default_phone_number": order.phone_number,
            "default_dob": order.dob,
            "default_gender": order.gender,
        }
        user_profile_form = UserProfileForm(profile_data, instance=profile)
        if user_profile_form.is_valid():
            user_profile_form.save()

    # Sends confirmation email

    cust_email = order.email
    subject = render_to_string(
        "signup/confirmation_emails/confirmation_email_subject.txt",
        {"order": order})

    body = render_to_string(
        "signup/confirmation_emails/confirmation_email_body.txt",
        {"order": order, "contact_email": settings.DEFAULT_FROM_EMAIL})
    send_mail(
        subject,
        body,
        settings.DEFAULT_FROM_EMAIL,
        [cust_email],
    )

    template = "signup/payment_success.html"
    context = {
        "order": order,
    }

    return render(request, template, context)
