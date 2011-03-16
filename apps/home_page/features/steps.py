# -*- coding: utf-8 -*-
from lettuce import step
from model_mommy.mommy import Mommy
from apps.news.models import News
from apps.projects.models import Project

@step(u'exist a news:')
def exist_a_news(step):
    for news_hashes in step.hashes:
        mom = Mommy(News, False)
        news = mom.make_one(title=news_hashes.get('title'), summary=news_hashes.get('summary'))
        

@step(u'exist a project:')
def exist_a_project(step):
    for project_hashes in step.hashes:
        mom = Mommy(Project, False)
        project = mom.make_one(name=project_hashes.get('name'), status=project_hashes.get('status'))
