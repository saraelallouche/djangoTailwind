from django.db import models
from django.urls import reverse


class Post(models.Model):
    created = models.DateTimeField(
        auto_now_add=True, editable=False
    )  # useful for audit of database
    last_updated = models.DateTimeField(
        auto_now=True, editable=False
    )  # useful for audit of database

    # blank, null and verbose are not mandatory, but it is helpful to define the values, if null=True including a default value could be useful
    title = models.CharField(
        max_length=200, blank=False, null=False, verbose_name="Title"
    )

    # always think on delete mode and related_name (author.posts access)
    author = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
        related_name="posts",
        blank=False,
        null=False,
        verbose_name="author",
    )
    body = models.TextField(blank=False, null=False, verbose_name="Body")

    class Meta:
        ordering = ["last_updated", "title"]  # useful to determine by default ordering
        verbose_name_plural = "Posts"  # verbose plural name in admin
        app_label = "crud"  # part of the app
        db_table = "crud_post"  # name of the table in the database

    def __str__(self):
        # check useful if field is not mandatory
        if self.title is None:
            return " "
        return self.title

    # By default success_url method called in class based-views
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
