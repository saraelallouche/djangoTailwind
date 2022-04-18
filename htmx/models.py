from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=255)
    is_done = models.BooleanField(default=False)


class Course(models.Model):
    name = models.CharField(max_length=128)


class Module(models.Model):
    name = models.CharField(max_length=128)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="modules")
