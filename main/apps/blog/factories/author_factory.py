from factory.django import DjangoModelFactory
from factory.faker import Faker


from main.apps.blog.models import Author


class AuthorFactory(DjangoModelFactory):
    name = Faker(provider="name")
    email = Faker(provider="email")

    class Meta:
        model = Author
