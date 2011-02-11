from django.db import models
from apps.teams.models import Team
from apps.projects.models import Project


class Participation(models.Model):
    member = models.ForeignKey('Member')
    project = models.ForeignKey(Project)
    start_date = models.DateField()
    end_date = models.DateField(null=True)

class Member(models.Model):
    name = models.CharField(max_length=100)
    currently_does = models.TextField()
    life_and_work = models.TextField()
    site = models.URLField(null=True)
    github = models.URLField(null=True)
    twitter = models.URLField(null=True)
    slideshare = models.URLField(null=True)
    lattes = models.URLField(null=True)
    photo = models.ImageField(upload_to='images/members')
    started_nsi_date = models.DateField()
    desertion_nsi_date = models.DateField(null=True)
