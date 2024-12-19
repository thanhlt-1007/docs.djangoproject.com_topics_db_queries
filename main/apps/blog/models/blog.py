from django.db.models import Model, CharField, TextField


class Blog(Model):
    name = CharField(max_length=100)
    tagline = TextField()
