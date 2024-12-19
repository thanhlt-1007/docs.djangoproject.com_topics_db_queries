# Generated by Django 5.1.4 on 2024-12-19 09:23

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0002_author"),
    ]

    operations = [
        migrations.CreateModel(
            name="Entry",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("headline", models.CharField(max_length=255)),
                ("body_text", models.TextField()),
                ("pub_date", models.DateField()),
                ("mod_date", models.DateField(default=datetime.date.today)),
                ("number_of_comments", models.PositiveIntegerField(default=0)),
                ("number_of_pingbacks", models.PositiveIntegerField(default=0)),
                ("ratings", models.PositiveIntegerField(default=5)),
                ("authors", models.ManyToManyField(to="blog.author")),
                (
                    "blog",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="blog.blog"
                    ),
                ),
            ],
        ),
    ]
