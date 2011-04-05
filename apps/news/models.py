from datetime import datetime as dt
from django.db import models
from django.contrib.auth.models import User
from thumbs import ImageWithThumbsField
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

    def __unicode__(self):
        return self.title
