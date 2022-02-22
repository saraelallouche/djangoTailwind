from django import forms
from django.db.models import fields
from django.forms.widgets import RadioSelect
from .models import CustomUser


class CustomUserCreateForm(forms.Form):
    class Meta:
        model = CustomUser

        username = forms.CharField(max_length=30)
        about = forms.CharField(max_length=150)
        # image = forms.ImageField(upload_to="static_cdn/admin/img")
        firstname = forms.CharField(max_length=30)
        lastname = forms.CharField(max_length=30)
        email = forms.CharField(max_length=50)
        countries = (
            ("0", "United states"),
            ("1", "Canada"),
            ("2", "France"),
        )
        country = forms.ChoiceField(choices=countries, max_length=50)
        address = forms.CharField(max_length=50)
        city = forms.CharField(max_length=60)
        state = forms.CharField(max_length=30)
        zipcode = forms.IntegerField(
            max_length=8,
        )

        by_email_comments = forms.BooleanField("Comments")
        by_email_candidates = forms.BooleanField("Candidates")
        by_email_offers = forms.BooleanField("Offers")

        options = (
            ("0", "Everything"),
            ("1", "Same as email"),
            ("2", "No push notifications"),
        )

        notifications = forms.ChoiceField(choices=options, required=True)
        notifications = forms.ChoiceField(
            widget=RadioSelect(),
            choices=[
                (0, "Everything"),
                (1, "Same as email"),
                (2, "No push notifications"),
            ],
        )
