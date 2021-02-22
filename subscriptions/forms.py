from django import forms
from .models import Subscription, Category


class SubscriptionForm(forms.ModelForm):

    class Meta:
        model = Subscription
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields["category"].choice = friendly_names


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = "__all__"
