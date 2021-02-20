from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings
from .models import SubscriptionDetails
from subscriptions.models import Subscription

from .forms import SignupForm

from profiles.forms import UserProfileForm
from profiles.models import UserProfile

import stripe


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
            messages.error(request, "There was an error with your form. \
            Please check your information.")

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

    # from https://courses.codeinstitute.net/courses/course-v1:CodeInstitute+FSF_102+Q1_2020/courseware/4201818c00aa4ba3a0dae243725f6e32/90cda137ebaa461894ba8c89cd83291a/
    if not stripe_public_key:
        messages.warning(request, "Stripe public key is missing. \
        Did you forget to set it in the environment?")

    template = "signup/signup.html"

    context = {
        "stripe_public_key": stripe_public_key,
        "client_secret": intent.client_secret,
        "signup_form": signup_form,
        "price": subscription_price,
        "sub_id": sub_id
    }

    return render(request, template, context)


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

    messages.success(request, f"Signup Successful! Your order number is {order_number}.\
    A confirmation email will be sent to {order.email}.")

    template = "signup/payment_success.html"
    context = {
        "order": order,
    }

    return render(request, template, context)
