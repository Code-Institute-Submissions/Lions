from django.shortcuts import render, redirect, reverse
from .forms import SignupForm
# Create your views here.


def signup(request):
    signup_form = SignupForm
    template = "signup/signup.html"
    context = {
        "signup_form": signup_form,
        "stripe_public_key": "pk_test_51IAbyUCU1rp8UcNhz7wyJHGItLEUX2Dlxmo85tGnMF0P2qG7F4Hp4T0gneJNXOPj9Cf3ZcrWH7Vnai8hBvZIITAi00si3GnT38",
    }

    return render(request, template, context)
