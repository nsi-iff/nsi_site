from django.db import models


PROJECT_STATES = (
    ('aberto', 'aberto'),
    ('cancelado', 'cancelado'),
    ('finalizado', 'finalizado'),
    ('paralisado', 'paralisado'))


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    logo = models.ImageField(upload_to='images/projects', null=True, blank=True)
    sponsor = models.CharField(max_length=100)
    status = models.CharField(max_length=100, choices=PROJECT_STATES)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    def finished(self):
        return self.end_date is not None

    def __unicode__(self):
        return self.name
        
    def save(self, *args, **kwargs):
        if self.finished():
            self.status = 'finalizado'
            super(Project, self).save(*args, **kwargs)
        else:
            super(Project, self).save(*args, **kwargs)

class Document(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    file = models.FileField(upload_to='files/projects')
    project = models.ForeignKey(Project)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title + ' - ' + self.description
