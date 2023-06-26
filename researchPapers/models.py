from django.db import models

class researchPaper(models.Model):
    title = models.TextField(max_length=120)
    author = models.TextField(blank=False, null=False)
    description = models.TextField(blank=False, null=False)

