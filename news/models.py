from django.db import models
from django.contrib.auth.models import User

class News(models.Model):
    title = models.CharField(max_length=200)
    summary = models.CharField(max_length=200, null=True, blank=True)
    body = models.TextField()
    image = models.ImageField(null=True, blank=True, upload_to='images')
    author = models.ForeignKey(User)
    datetime = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = 'News'
        
    def __uniicode__(self):
        return self.title