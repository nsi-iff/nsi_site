from django.db import models


class WikiItem(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    slug = models.SlugField(max_length=100, blank=True)
