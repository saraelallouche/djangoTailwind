from django.db import models
from htmx.models.course import Course, Module


class Todo(models.Model):
    created = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        null=True,
    )
    last_updated = models.DateTimeField(
        auto_now=True,
        editable=False,
        null=True,
    )
    title = models.CharField(
        max_length=255, blank=False, null=False, verbose_name="Title"
    )

    course = models.ForeignKey(
        Course, null=True, on_delete=models.CASCADE, related_name="todos"
    )
    module = models.ForeignKey(
        Module, null=True, on_delete=models.CASCADE, related_name="todos"
    )
    is_done = models.BooleanField(default=False)

    class Meta:
        ordering = ["last_updated", "title"]  # useful to determine by default ordering
        verbose_name_plural = "Todos"  # verbose plural name in admin
        app_label = "htmx"  # part of the app

    def __str__(self):
        return self.title
