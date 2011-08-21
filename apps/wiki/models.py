from django.db import models
from django.db.models import signals
from django.template.defaultfilters import slugify


class WikiItem(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    slug = models.SlugField(max_length=100, blank=True)


def wiki_item_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.title)

signals.pre_save.connect(wiki_item_pre_save, sender=WikiItem)
