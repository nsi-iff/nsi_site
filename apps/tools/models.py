from django.db import models
from django.template.defaultfilters import slugify
from apps.projects.models import Project


TOOLS_STATES = (
    ('ativo', 'ativo'),
    ('descontinuado', 'descontinuado'))

class Tool(models.Model):
    name = models.CharField(max_length=100)
    short_description = models.TextField(max_length=200)
    description = models.TextField()
    repository = models.CharField(max_length=100)
    site = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='images/tools', null=True, blank=True)
    status = models.CharField(max_length=100, choices=TOOLS_STATES)
    highlight = models.BooleanField()
    relateds_projects = models.ManyToManyField(Project, null=True, blank=True)
    slug = models.SlugField(max_length=100, blank=True)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Tool, self).save(*args, **kwargs)

