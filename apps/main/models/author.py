from django.db import models


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
