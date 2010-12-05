from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    situation = models.CharField(max_length=200)
    start_date = models.CharField(max_length=200)
    end_date = models.CharField(max_length=200)
