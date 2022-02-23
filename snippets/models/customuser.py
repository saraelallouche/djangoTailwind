from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class CustomUser(models.Model):

    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    username = models.CharField(max_length=30)
    about = models.TextField(max_length=150)
    image = models.ImageField(upload_to="images", null=True, blank=True)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    countries = (
        ("0", "United states"),
        ("1", "Canada"),
        ("2", "France"),
    )
    country = models.CharField(max_length=10, choices=countries)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state = models.CharField(max_length=30, verbose_name="State/Province")
    zipcode = models.PositiveIntegerField(verbose_name="Zip/Postal code")

    by_email_comments = models.BooleanField("Comments", default=False)
    by_email_candidates = models.BooleanField("Candidates", default=False)
    by_email_offers = models.BooleanField("Offers", default=False)

    options = (
        ("0", "Everything"),
        ("1", "Same as email"),
        ("2", "No push notifications"),
    )
    notifications = models.CharField(
        max_length=2, choices=options, null=True, blank=True, default=""
    )

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse("user_detail", args=[str(self.pk)])
