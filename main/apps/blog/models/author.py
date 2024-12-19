from django.db.models import Model, CharField, EmailField


class Author(Model):
    name = CharField(max_length=200)
    email = EmailField()
