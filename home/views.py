from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Slideshow
from .forms import SlideForm

# Create your views here.


def index(request):
    """ A view to return the index page """

    slides = Slideshow.objects.all()

    context = {
        "slides": slides
    }

    return render(request, "home/index.html", context)


@login_required
def all_slides(request):
    """ A view to return all slides """

    if not request.user.is_superuser:
        return redirect(reverse("home"))

    slides = Slideshow.objects.all()

    context = {
        "slides": slides
    }

    return render(request, "home/slides.html", context)


@login_required
def add_slide(request):
    """ Add a new slide to the slideshow """

    if not request.user.is_superuser:
        return redirect(reverse("home"))

    if request.method == "POST":
        form = SlideForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    form = SlideForm()
    template = "home/add_slide.html"
    context = {
        "form":  form
    }

    return render(request, template, context)


@login_required
def edit_slide(request, slide_id):
    """ Edit a slide in the slideshow """

    if not request.user.is_superuser:
        return redirect(reverse("home"))

    slide = get_object_or_404(Slideshow, pk=slide_id)
    if request.method == "POST":
        form = SlideForm(request.POST, request.FILES, instance=slide)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = SlideForm(instance=slide)

    template = "home/edit_slide.html"
    context = {
        "form":  form,
        "slide": slide,
    }

    return render(request, template, context)


@login_required
def delete_slide(request, slide_id):
    """ delete a slide from the slideshow """

    if not request.user.is_superuser:
        return redirect(reverse("home"))

    slide = get_object_or_404(Slideshow, pk=slide_id)
    slide.delete()
    return redirect("home")
