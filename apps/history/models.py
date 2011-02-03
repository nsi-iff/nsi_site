from django.db import models
from docutils.core import publish_parts

class History(models.Model):
    text = models.TextField(blank=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'histories'

    def to_html(self):
        parts = publish_parts(source=self.text, writer_name="html4css1")
        return parts['fragment']

