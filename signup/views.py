from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings
from subscriptions.models import Subscription

from .forms import SignupForm

import stripe


def signup(request):

    signup_form = SignupForm
    if request.method == "POST":
        form = signup_form(request.POST)
        if form.is_valid():
            subscription_type = form.cleaned_data["subscription_type"]

            price = int(subscription_type.price * 100)

            sub = request.session.get("sub", {})

            sub["subscription_type"] = subscription_type.name
            sub["price"] = price

            request.session["sub"] = sub

            return redirect(payment)

    template = "signup/signup.html"
    context = {
        "signup_form": signup_form,
    }

    return render(request, template, context)


def payment(request):
        stripe_public_key = settings.STRIPE_PUBLIC_KEY
        stripe_secret_key = settings.STRIPE_SECRET_KEY

        stripe_total = request.session["sub"]["price"]

        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        # from https://courses.codeinstitute.net/courses/course-v1:CodeInstitute+FSF_102+Q1_2020/courseware/4201818c00aa4ba3a0dae243725f6e32/90cda137ebaa461894ba8c89cd83291a/
        if not stripe_public_key:
            messages.warning(request, "Stripe public key is missing. Did you forget to set it in the environment?")

        template = "signup/payment.html"
        context = {
            "stripe_public_key": stripe_public_key,
            "client_secret": intent.client_secret,
        }

        return render(request, template, context)
