from django import forms
from .models import Participant


class AzeoidRegistrationForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = (
            "fname",
            "lname",
            "email",
            "phone",
            "alt_phone",
            "curr_year",
            "university",
            "address",
            "pincode",
            "state",
        )

        widgets = {
            "fname": forms.TextInput(attrs={"class": "form-input"}),
            "lname": forms.TextInput(attrs={"class": "form-input"}),
            "email": forms.TextInput(attrs={"class": "form-input"}),
            "phone": forms.TextInput(attrs={"class": "form-input"}),
            "alt_phone": forms.TextInput(attrs={"class": "form-input"}),
            "curr_year": forms.TextInput(attrs={"class": "form-input"}),
            "university": forms.TextInput(attrs={"class": "form-input"}),
            "address": forms.Textarea(attrs={"class": "form-textarea", "rows": 4}),
            "pincode": forms.TextInput(attrs={"class": "form-input"}),
            "state": forms.TextInput(attrs={"class": "form-input"}),
        }
