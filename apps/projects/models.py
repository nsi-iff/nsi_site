from django.db import models


PROJECT_STATES = (
    ('aberto', 'aberto'),
    ('cancelado', 'cancelado'),
    ('finalizado', 'finalizado'),
    ('paralisado', 'paralisado'))


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    logo = models.ImageField(upload_to='images/projects')
    sponsor = models.CharField(max_length=100)
    status = models.CharField(max_length=100, choices=PROJECT_STATES)
    start_date = models.DateField()
    end_date = models.DateField(null=True)

    def finished(self):
        return self.end_date is not None


class Document(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    file = models.FileField(upload_to='files/projects')
    project = models.ForeignKey(Project)
    uploaded_at = models.DateTimeField(auto_now_add=True)

