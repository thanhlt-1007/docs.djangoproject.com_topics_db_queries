from factory.django import DjangoModelFactory
from factory.faker import Faker


class BlogFactory(DjangoModelFactory):
    name = Faker(provider="sentence")
    tagline = Faker(provider="text")

    class Meta:
        model = "blog.Blog"
