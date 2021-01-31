from django.shortcuts import render
from .models import Slideshow

# Create your views here.


def index(request):
    """ A view to return the index page """

    slides = Slideshow.objects.all()

    context = {
        "slides": slides
    }

    return render(request, "home/index.html", context)
