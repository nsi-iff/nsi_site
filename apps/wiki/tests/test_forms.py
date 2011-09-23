from django.test import TestCase

from should_dsl import should

from apps.wiki.forms import WikiItemForm
from apps.wiki.models import WikiItem


class WikiFormsTests(TestCase):

    def setUp(self):
        self.wiki_item_form = WikiItemForm()

    def test_it_is_an_instance_of_WikiItem(self):
        self.wiki_item_form.instance |should| be_instance_of(WikiItem)

    def test_it_has_title_and_content(self):
        self.wiki_item_form.fields.keys() |should| equal_to(['title', 'content'])
        self.wiki_item_form.fields.keys() |should| have(2).fields
