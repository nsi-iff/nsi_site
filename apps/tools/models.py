from django.db import models
from apps.projects.models import Project

class Tool(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    repository = models.CharField(max_length=100)
    site = models.CharField(max_length=100)
    highlight = models.BooleanField()
    relateds_projects = models.ManyToManyField(Project, null=True, blank=True)
    
    def __unicode__(self):
        return self.name
