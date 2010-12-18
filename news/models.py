from django.db import models

class News(models.Model):
    title = models.CharField(max_length=200)
    summary = models.CharField(max_length=200)
    body = models.TextField()
    image = models.ImageField(upload_to='images/news')
    publication_date = models.DateField()

