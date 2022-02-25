from django import forms
from ..models import CustomUserModel


class CustomUser(forms.ModelForm):

    username = forms.CharField()
    about = forms.CharField()
    image = forms.ImageField(required=False)
    firstname = forms.CharField()
    lastname = forms.CharField()
    email = forms.CharField()
    countries = [
        ("USA", "United states"),
        ("CA", "Canada"),
        ("FR", "France"),
    ]

    country = forms.ChoiceField(choices=countries)
    address = forms.CharField()
    city = forms.CharField()
    state = forms.CharField()
    zipcode = forms.IntegerField()

    email_options = [
        ("0", "Comments"),
        ("1", "Candidates"),
        ("2", "Offers"),
    ]
    by_email = forms.MultipleChoiceField(
        required=False, widget=forms.RadioSelect(choices=email_options)
    )

    options = [
        ("0", "Everything"),
        ("1", "Same as email"),
        ("2", "No push notifications"),
    ]
    notifications = forms.ChoiceField(
        required=False, widget=forms.RadioSelect, choices=options
    )

    class Meta:
        model = CustomUserModel
        fields = [
            "username",
            "about",
            "image",
            "firstname",
            "lastname",
            "email",
            "country",
            "address",
            "city",
            "state",
            "zipcode",
            "notifications",
        ]
