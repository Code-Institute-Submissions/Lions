from django.shortcuts import render, redirect, reverse
from .forms import SignupForm
# Create your views here.


def signup(request):
    signup_form = SignupForm
    template = "signup/signup.html"
    context = {
        "signup_form": signup_form
    }

    return render(request, template, context)
