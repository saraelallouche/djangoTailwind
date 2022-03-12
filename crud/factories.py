import factory
from factory.django import DjangoModelFactory

from .models import Post

# Defining a factory
class PostFactory(DjangoModelFactory):
    class Meta:
        model = Post

    title = factory.Faker("company")
    body = factory.Faker("paragraph")
