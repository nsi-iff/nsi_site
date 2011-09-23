# -*- coding: utf-8 -*-

from django.contrib.auth.models import User

from lettuce import step, world
from lettuce.django import django_url
from should_dsl import should

from apps.wiki.models import WikiItem


@step(u'exist a wiki item:')
def exist_a_wiki_item(step):
    for wiki_item in step.hashes:
        WikiItem(id=wiki_item['id'], title=wiki_item['title'], content=wiki_item['content']).save()

@step(u'I should have a link that ends in "(.*)"')
def i_should_have_a_link_with_ends_in(step, url):
    links = world.browser.find_by_tag('a')
    end_links = [end_link for end_link in links if end_link['href'].endswith(url)]
    end_links |should| have_at_least(1).end_link

@step(u'I click on link that ends in "(.*)"')
def i_click_on_link_that_ends_in(step, url):
    links = world.browser.find_by_tag('a')
    end_link = [end_link for end_link in links if end_link['href'].endswith(url)]
    end_link |should| have(1).end_link
    end_link[0].click()

@step(u"that i'm logged in")
def that_i_m_logged_in(step):
    user = User.objects.create_user('test', 'test@test.com', 'test')
    user.is_staff = True
    user.save()
    world.browser.visit(django_url('/admin'))
    world.browser.fill('username', 'test')
    world.browser.fill('password', 'test')
    world.browser.find_by_value('Acessar').first.click()
