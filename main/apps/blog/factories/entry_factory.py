from factory.django import DjangoModelFactory
from factory import SubFactory
from factory.faker import Faker


class EntryFactory(DjangoModelFactory):
    blog = SubFactory(factory="main.apps.blog.factories.BlogFactory")
    headline = Faker(provider="sentence")
    body_text = Faker(provider="text")
    pub_date = Faker(provider="date_object")
    mod_date = Faker(provider="date_object")
    number_of_comments = Faker(provider="pyint")
    number_of_comments = Faker(provider="pyint")
    ratings = Faker(provider="pyint")

    class Meta:
        model = "blog.Entry"
