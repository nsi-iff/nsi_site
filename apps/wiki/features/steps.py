# -*- coding: utf-8 -*-

from lettuce import step, world
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
