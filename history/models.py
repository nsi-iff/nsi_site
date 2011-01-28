from django.db import models


class History(models.Model):
    text = models.TextField(blank=False)
    updated_at = models.DateTimeField(auto_now=True)

