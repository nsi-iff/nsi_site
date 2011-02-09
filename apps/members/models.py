from django.db import models
from apps.teams.models import Team
from apps.projects.models import Project

class Member(models.Model):
    name = models.CharField(max_length=100)
    #current_team = models.ManyToManyField(Team)
    current_team = models.CharField(max_length=100)
    currently_does = models.TextField()
    life_and_work =  models.TextField()
    site = models.URLField(null=True)
    github = models.URLField(null=True)
    twitter = models.URLField(null=True)
    slideshare = models.URLField(null=True)
    lattes = models.URLField(null=True)
    photo = models.ImageField(upload_to='images/members')
    #project_memberships = models.ManyToManyField(Project)
    project_memberships = models.CharField(max_length=100)
    started_nsi_date = models.DateField()
    desertion_nsi_date = models.DateField(null=True)
    
