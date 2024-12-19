from factory.django import DjangoModelFactory
from factory.faker import Faker


class AuthorFactory(DjangoModelFactory):
    name = Faker(provider="name")
    email = Faker(provider="email")

    class Meta:
        model = "blog.Author"
