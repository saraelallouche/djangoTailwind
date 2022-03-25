from django.db import models

from django.urls.base import reverse


class File(models.Model):
    file = models.FileField(upload_to="file/", default=None, verbose_name="file")
    names = (
        ("USA", "United states"),
        ("CA", "Canada"),
        ("FR", "France"),
    )
    name = models.CharField(max_length=10, choices=names)

    def __str__(self):
        return self.name

    # def get_absolute_url(self):  # new
    #     return reverse("detail_document", args=[str(self.id)])
