import time

from django.db import models


class Course(models.Model):
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
    name = models.CharField(
        max_length=128, blank=False, null=False, verbose_name="Name"
    )

    class Meta:
        ordering = ["name", "last_updated"]  # useful to determine by default ordering
        verbose_name_plural = "Courses"  # verbose plural name in admin
        app_label = "htmx"  # part of the app

    def __str__(self):
        return self.name


class Module(models.Model):
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
    name = models.CharField(
        max_length=128, blank=False, null=False, verbose_name="Name"
    )
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="modules")

    class Meta:
        ordering = ["name", "last_updated"]  # useful to determine by default ordering
        verbose_name_plural = "Modules"  # verbose plural name in admin
        app_label = "htmx"  # part of the app

    def __str__(self):
        return self.name
