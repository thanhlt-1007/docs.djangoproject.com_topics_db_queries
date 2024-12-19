from django.db.models import (
    Model,
    ForeignKey,
    CASCADE,
    CharField,
    TextField,
    DateField,
    ManyToManyField,
    PositiveIntegerField,
)

from datetime import date


class Entry(Model):
    blog = ForeignKey(to="blog.Blog", on_delete=CASCADE)
    authors = ManyToManyField(to="blog.Author")
    headline = CharField(max_length=255)
    body_text = TextField()
    pub_date = DateField()
    mod_date = DateField(default=date.today)
    number_of_comments = PositiveIntegerField(default=0)
    number_of_pingbacks = PositiveIntegerField(default=0)
    ratings = PositiveIntegerField(default=5)
