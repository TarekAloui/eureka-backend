# Generated by Django 4.2.4 on 2023-08-12 03:27

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("main", "0002_remove_paper_authors_remove_paper_relatedtweets_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Author",
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
                ("name", models.CharField(max_length=255)),
                (
                    "affiliation",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("hIndex", models.PositiveIntegerField()),
                ("i10Index", models.PositiveIntegerField()),
                ("citations", models.PositiveIntegerField()),
                ("interests", models.TextField(blank=True, null=True)),
                ("profileUrl", models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name="Tweet",
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
                ("url", models.URLField()),
                ("user_name", models.CharField(max_length=255)),
                ("retweets", models.PositiveIntegerField()),
                ("likes", models.PositiveIntegerField()),
                ("text", models.TextField()),
                ("date", models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name="Paper",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("abstract", models.TextField()),
                ("pub_date", models.DateTimeField()),
                ("updated_date", models.DateTimeField()),
                ("categories", models.TextField(blank=True, null=True)),
                ("links", models.TextField(blank=True, null=True)),
                ("comment", models.TextField(blank=True, null=True)),
                (
                    "journal_ref",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("trendiness_score", models.FloatField()),
                ("authors", models.ManyToManyField(to="main.author")),
                ("relatedTweets", models.ManyToManyField(to="main.tweet")),
            ],
        ),
    ]
