from factory.django import DjangoModelFactory
from factory.faker import Faker


from main.apps.blog.models import Blog


class BlogFactory(DjangoModelFactory):
    name = Faker(provider="sentence")
    tagline = Faker(provider="text")

    class Meta:
        model = Blog
