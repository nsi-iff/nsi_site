from django.db import models
from django.template.defaultfilters import slugify
from thumbs import ImageWithThumbsField
from apps.projects.models import Project


MEMBER_FUNCTIONS = (
    ('0', 'gerente'),
    ('1', 'coordenador'),
    ('2', 'pesquisador'),
    ('3', 'bolsista'),
    ('4', 'colaborador'))


class Participation(models.Model):
    member = models.ForeignKey('Member')
    project = models.ForeignKey(Project)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    def __unicode__(self):
        return self.member.name + ' - ' + self.project.name

class Member(models.Model):
    name = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100, null=True, blank=True)
    currently_does = models.TextField()
    life_and_work = models.TextField()
    function = models.CharField(max_length=100, choices=MEMBER_FUNCTIONS)
    site = models.URLField(null=True, blank=True)
    github = models.CharField(max_length=50, null=True, blank=True)
    twitter = models.CharField(max_length=50, null=True, blank=True)
    slideshare = models.CharField(max_length=50, null=True, blank=True)
    lattes = models.URLField(null=True, blank=True)
    photo = ImageWithThumbsField(upload_to='images/members', sizes=((100, 100), ))
    started_nsi_date = models.DateField()
    desertion_nsi_date = models.DateField(null=True, blank=True)
    is_renegade = models.BooleanField(editable=False)
    slug = models.SlugField(max_length=100, blank=True)

    def github_link(self):
        github_site = "http://github.com/"
        return github_site + self.github

    def github_feed(self):
        return self.github_link() + '.atom'

    def twitter_link(self):
        twitter_site = "http://twitter.com/"
        return twitter_site + self.twitter

    def slideshare_link(self):
        slideshare_site = "http://www.slideshare.net/"
        return slideshare_site + self.slideshare

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        if self.desertion_nsi_date is not None:
            self.is_renegade = True
            super(Member, self).save(*args, **kwargs)
        else:
            self.is_renegade = False
            super(Member, self).save(*args, **kwargs)

