from django import forms
from .models import SubscriptionDetails


class SignupForm(forms.ModelForm):
    class Meta:
        model = SubscriptionDetails
        fields = (
            "full_name",
            "email",
            "phone_number",
            "subscription_type",
            "dob",
            "gender",
        )

    def __init__(self, *args, **kwargs):
        # from https://courses.codeinstitute.net/courses/course-v1:CodeInstitute+FSF_102+Q1_2020/courseware/4201818c00aa4ba3a0dae243725f6e32/326f171b831446588d33c0333eb4caaa/
        """
        Add placeholders and classes, remove auto generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            "full_name": "Full Name",
            "email": "Email",
            "phone_number": "Phone Number",
            "dob": "DOB",
            "gender": "Gender",
            "subscription_type": "Subscription Type"
        }

        self.fields["full_name"].widget.attrs["autofocus"] = True
        self.fields['subscription_type'].widget = forms.HiddenInput()

        for field in self.fields:
            if self.fields[field].required:
                placeholder = f"{placeholders[field]} *"
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs["placeholder"] = placeholder
            self.fields[field].widget.attrs["class"] = "stripe-stype-input"
            self.fields[field].label = False
