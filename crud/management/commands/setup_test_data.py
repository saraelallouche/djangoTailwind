# https://mattsegal.dev/django-factoryboy-dummy-data.html

import random

from django.db import transaction
from django.core.management.base import BaseCommand

from ...models import Post
from ...factories import (
    PostFactory,
)

NUM_POST = 15000


class Command(BaseCommand):
    help = "Generates test data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        models = [Post]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Creating new data...")
        # Create all the posts
        for _ in range(NUM_POST):
            post = PostFactory()
