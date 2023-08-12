from django.db import models
import uuid


class Author(models.Model):
    name = models.CharField(max_length=255)
    affiliation = models.CharField(
        max_length=255, blank=True, null=True
    )  # Can be blank or null
    hIndex = models.PositiveIntegerField()
    i10Index = models.PositiveIntegerField()
    citations = models.PositiveIntegerField()
    interests = models.TextField(
        blank=True, null=True
    )  # Store interests as comma-separated values
    profileUrl = models.URLField()


class Tweet(models.Model):
    url = models.URLField()
    user_name = models.CharField(max_length=255)
    retweets = models.PositiveIntegerField()
    likes = models.PositiveIntegerField()
    text = models.TextField()
    date = models.DateTimeField()


class Paper(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    title = models.CharField(max_length=255)
    authors = models.ManyToManyField(Author)
    abstract = models.TextField()
    pub_date = models.DateTimeField()
    updated_date = models.DateTimeField()
    categories = models.TextField(
        blank=True, null=True
    )  # Store categories as comma-separated values
    links = models.TextField(
        blank=True, null=True
    )  # Store links as comma-separated values
    comment = models.TextField(blank=True, null=True)
    journal_ref = models.CharField(max_length=255, blank=True, null=True)
    trendiness_score = models.FloatField()
    relatedTweets = models.ManyToManyField(Tweet)
