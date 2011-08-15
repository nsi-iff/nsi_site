from django.test import TestCase

from apps.wiki.models import WikiItem

from should_dsl import should


class WikiModelsTest(TestCase):

    def test_it_has_title_and_content(self):
        self.wiki_item = WikiItem(title='Add Plone Site', content='Click on "Add Plone Site"')
        self.wiki_item.title |should| equal_to('Add Plone Site')
        self.wiki_item.content |should| equal_to('Click on "Add Plone Site"')
