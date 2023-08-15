from django.db import models
import uuid
from .tweet import Tweet
from .author import Author


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
