from django import forms


class CustomUser(forms.Form):

    created = forms.DateTimeField(auto_now_add=True, editable=False)
    last_updated = forms.DateTimeField(auto_now=True, editable=False)
    username = forms.CharField(max_length=30)
    about = forms.CharField(max_length=150)
    image = forms.ImageField(upload_to="media", null=True, blank=True)
    firstname = forms.CharField(max_length=30)
    lastname = forms.CharField(max_length=30)
    email = forms.CharField(max_length=50)
    countries = (
        ("0", "United states"),
        ("1", "Canada"),
        ("2", "France"),
    )
    country = forms.ChoiceField(max_length=10, choices=countries)
    address = forms.CharField(max_length=50)
    city = forms.CharField(max_length=60)
    state = forms.CharField(max_length=30, verbose_name="State/Province")
    zipcode = forms.IntegerField(verbose_name="Zip/Postal code")

    by_email_comments = forms.BooleanField("Comments", default=False)
    by_email_candidates = forms.BooleanField("Candidates", default=False)
    by_email_offers = forms.BooleanField("Offers", default=False)

    options = (
        ("0", "Everything"),
        ("1", "Same as email"),
        ("2", "No push notifications"),
    )
    notifications = forms.ChoiceField(
        max_length=1, widget=forms.RadioSelect(choices=options), default=""
    )
