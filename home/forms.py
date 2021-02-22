from django import forms
from .models import Slideshow


class SlideForm(forms.ModelForm):

    class Meta:
        model = Slideshow
        fields = '__all__'
