from django.test import TestCase, Client

from should_dsl import should


class WikiViewsTests(TestCase):

    def setUp(self):
        self.client = Client()

    def test_it_shows_all_items(self):
        response = self.client.get('/wiki/')
        response.status_code |should| equal_to(200)
        response.template[0].name |should| equal_to('wiki_items.html')
        response.context[0].has_key('wiki_items') |should| equal_to(True)

    def test_it_adds_an_item(self):
        response = self.client.get('/wiki/novo_item/')
        response.status_code |should| equal_to(200)
        response.template[0].name |should| equal_to('add_wiki_item.html')
        response.context[0].has_key('wiki_item_form') |should| equal_to(True)
