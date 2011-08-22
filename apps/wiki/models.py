from django.db import models
from django.db.models import signals
from django.template.defaultfilters import slugify


class WikiItem(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    slug = models.SlugField(max_length=100, blank=True, unique=True)


def wiki_item_pre_save(signal, instance, sender, **kwargs):
    slug = slugify(instance.title)
    new_slug = slug
    counter = 0

    while WikiItem.objects.filter(slug=new_slug).exclude(id=instance.id).count() > 0:
        counter += 1
        new_slug = '%s-%d' % (slug, counter)

    instance.slug = new_slug


signals.pre_save.connect(wiki_item_pre_save, sender=WikiItem)
