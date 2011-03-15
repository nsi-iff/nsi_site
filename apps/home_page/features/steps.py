# -*- coding: utf-8 -*-
from lettuce import step
from model_mommy.mommy import Mommy
from apps.news.models import News

@step(u'exist a news:')
def exist_a_news(step):
    for news_hashes in step.hashes:
        mom = Mommy(News, False)
        news = mom.make_one(title=news_hashes.get('title'))
