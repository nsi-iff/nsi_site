from django.db import models
from docutils.core import publish_parts


class NSIInfo(models.Model):
    history = models.TextField(blank=False)
    summary = models.TextField(blank=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'nsi_info'

    def history_as_html(self):
        return self._to_html(self.history)

    def summary_as_html(self):
        return self._to_html(self.summary)

    def _to_html(self, rst_source):
        parts = publish_parts(source=rst_source, writer_name="html4css1")
        return parts['fragment']

