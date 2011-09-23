from django.test import TestCase, Client
from django.contrib.auth.models import User

from should_dsl import should

from apps.wiki.models import WikiItem


class WikiViewsTests(TestCase):

    def setUp(self):
        self.client = Client()
        user = User.objects.create_user('test', 'test@test.com', 'test').save()

    def test_it_shows_all_wiki_items(self):
        response = self.client.get('/wiki/')
        response.status_code |should| equal_to(200)
        response.template[0].name |should| equal_to('wiki_items.html')
        response.context[0].has_key('wiki_items') |should| equal_to(True)

    def test_it_can_add_a_wiki_item(self):
        self.client.login(username='test', password='test')
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
        response = self.client.get('/wiki/add-plone-site/')
        response.status_code |should| equal_to(200)
        response.template[0].name |should| equal_to('wiki_item.html')
        response.context[0].has_key('wiki_item') |should| be(True)

    def test_it_can_edit_a_wiki_item(self):
        self.client.login(username='test', password='test')
        WikiItem(id=3, title='Add Plone Site', content='Click on "Add Plone Site"').save()
        wiki_item = WikiItem.objects.get(pk=3)
        response = self.client.get('/wiki/add-plone-site/editar/')
        response.status_code |should| equal_to(200)
        response.template[0].name |should| equal_to('edit_wiki_item.html')
        response.context[0].has_key('form') |should| be(True)

    def test_it_can_delete_a_wiki_item(self):
        self.client.login(username='test', password='test')
        WikiItem(id=3, title='Add Plone Site', content='Click on "Add Plone Site"').save()
        wiki_item = WikiItem.objects.get(pk=3)
        response = self.client.get('/wiki/add-plone-site/excluir/')
        response.status_code |should| equal_to(200)
        response.template[0].name |should| equal_to('delete_wiki_item.html')
        response.context[0].has_key('object') |should| be(True)
