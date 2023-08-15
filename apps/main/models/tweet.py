from django.db import models


class Tweet(models.Model):
    url = models.URLField()
    user_name = models.CharField(max_length=255)
    retweets = models.PositiveIntegerField()
    likes = models.PositiveIntegerField()
    text = models.TextField()
    date = models.DateTimeField()
