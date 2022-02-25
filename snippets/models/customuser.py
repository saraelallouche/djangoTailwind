from django.db import models
from django.core.validators import FileExtensionValidator


class CustomUserModel(models.Model):

    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    username = models.CharField(max_length=30)
    about = models.TextField(max_length=150)
    image = models.ImageField(
        upload_to="media",
        null=True,
        blank=True,
        validators=[FileExtensionValidator(["jpg", "png", "jpeg"])],
    )
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    countries = (
        ("USA", "United states"),
        ("CA", "Canada"),
        ("FR", "France"),
    )
    country = models.CharField(max_length=10, choices=countries)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state = models.CharField(max_length=30, verbose_name="State/Province")
    zipcode = models.PositiveIntegerField(verbose_name="Zip/Postal code")

    # by_email_comments = models.BooleanField("Comments", default=False)
    # by_email_candidates = models.BooleanField("Candidates", default=False)
    # by_email_offers = models.BooleanField("Offers", default=False)
    email_options = (
        ("0", "Comments"),
        ("1", "Candidates"),
        ("2", "Offers"),
    )
    by_email = models.CharField(
        max_length=1,
        choices=email_options,
        null=True,
        blank=True,
    )
    options = (
        ("0", "Everything"),
        ("1", "Same as email"),
        ("2", "No push notifications"),
    )
    notifications = models.CharField(
        max_length=1,
        choices=options,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.username

    # def get_absolute_url(self):
    #     return reverse("user_detail")
