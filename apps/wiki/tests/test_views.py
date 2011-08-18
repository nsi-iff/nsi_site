from django.test import TestCase, Client

from should_dsl import should

from apps.wiki.models import WikiItem


class WikiViewsTests(TestCase):

    def setUp(self):
        self.client = Client()

    def test_it_shows_all_wiki_items(self):
        response = self.client.get('/wiki/')
        response.status_code |should| equal_to(200)
        response.template[0].name |should| equal_to('wiki_items.html')
        response.context[0].has_key('wiki_items') |should| equal_to(True)

    def test_it_can_add_a_wiki_item(self):
        response = self.client.get('/wiki/novo_item/')
        response.status_code |should| equal_to(200)
        response.template[0].name |should| equal_to('add_wiki_item.html')
        response.context[0].has_key('wiki_item_form') |should| equal_to(True)

    def test_it_adds_a_wiki_item(self):
        response = self.client.post(
            '/wiki/novo_item/',
            {'title':'Adding a Plone Site', 'content': 'Just clik "Add Plone Site"'})
        response.status_code |should| equal_to(302)

    def test_it_can_view_a_wiki_item(self):
        wiki_item = WikiItem(id=3, title='Add Plone Site', content='Click on "Add Plone Site"').save()
        response = self.client.get('/wiki/3/')
        response.status_code |should| equal_to(200)
        response.template[0].name |should| equal_to('wiki_item.html')
        response.context[0].has_key('wiki_item') |should| be(True)
