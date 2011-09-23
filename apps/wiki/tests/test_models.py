from django.test import TestCase

from apps.wiki.models import WikiItem

from should_dsl import should, should_not


class WikiModelsTests(TestCase):

    def test_it_has_title_and_content_and_slug(self):
        self.wiki_item = WikiItem(
            title='Add Plone Site',
            content='Click on "Add Plone Site"',
            slug='add-plone-site'
        )
        self.wiki_item.title |should| equal_to('Add Plone Site')
        self.wiki_item.content |should| equal_to('Click on "Add Plone Site"')
        self.wiki_item.slug |should| equal_to('add-plone-site')

    def test_it_can_has_a_blank_slug(self):
        self.wiki_item = WikiItem(
            title='Install Django',
            content='Run "pip install django".',
        )
        self.wiki_item.full_clean() |should_not| throw('ValidationError')

    def test_it_fills_slug_with_title_when_pre_save_wiki_item(self):
        self.wiki_item = WikiItem(
            title='Add Plone Site', content='Click on "Add Plone Site"').save()
        self.wiki_item = WikiItem.objects.get(title='Add Plone Site')
        self.wiki_item.slug |should| equal_to('add-plone-site')

    def test_it_can_adds_many_wiki_items_with_same_title(self):
        self.first_wiki_item = WikiItem(
            id=1, title='Add Plone Site', content='Click on "Add Plone Site"').save()
        self.first_wiki_item = WikiItem.objects.get(id=1)
        self.first_wiki_item.slug |should| equal_to('add-plone-site')
        self.second_wiki_item = WikiItem(
            id=2, title='Add Plone Site', content='Second way to add Plone Site').save()
        self.second_wiki_item = WikiItem.objects.get(id=2)
        self.second_wiki_item.slug |should| equal_to('add-plone-site-1')
