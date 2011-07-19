from datetime import datetime as dt
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from thumbs import ImageWithThumbsField
from docutils.core import publish_parts
from apps.projects.models import Project


class News(models.Model):

    class Meta:
        verbose_name_plural = 'News'
        ordering = ['-date_and_time']

    title = models.CharField(max_length=200)
    summary = models.CharField(max_length=200, null=True, blank=True)
    body = models.TextField()
    image = ImageWithThumbsField(null=True, blank=True, upload_to='images/news', sizes=((150, 150), (90, 90), ))
    author = models.ForeignKey(User)
    date_and_time = models.DateTimeField(default=dt.now())
    projects_relateds = models.ManyToManyField(Project, null=True, blank=True)
    slug = models.SlugField(max_length=200, blank=True)

    def __unicode__(self):
        return self.title

    def body_as_html(self):
        parts = publish_parts(source=self.body, writer_name="html4css1")
        return parts['fragment']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(News, self).save(*args, **kwargs)

