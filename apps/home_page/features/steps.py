# -*- coding: utf-8 -*-
import os
import shutil
from datetime import datetime
from django.conf import settings
from lettuce import step
from model_mommy import mommy
from apps.news.models import News
from apps.projects.models import Project
from apps.tools.models import Tool
from django.contrib.auth.models import User


@step(u'exist a author:')
def exist_a_author(step):
    for user in step.hashes:
        mommy.make_one(User, username=user.get('name'), email='a@a.com')

@step(u'exist a news:')
def exist_a_news(step):
    for news_hashes in step.hashes:
        author = User.objects.get(username__exact=news_hashes.get('author'))
        mom = mommy.Mommy(News, False)
        date, hour = news_hashes.get('date_and_time').split()
        day, month, year = date.split('/')
        hours, minutes = hour.split(':')
        date_time = datetime(int(year), int(month), int(day), int(hours), int(minutes))
        news = mom.make_one(title=news_hashes.get('title'), image=news_hashes.get('image'), author=author, date_and_time=date_time).save()
        file_name = news_hashes.get('image').split('/')[-1]
        shutil.copy2(os.path.join(settings.PROJECT_ROOT_PATH, 'apps', 'home_page',
                                  'features', 'resources', file_name),
                     os.path.join(settings.MEDIA_ROOT, 'test', 'images', 'news'))

@step(u'exist a project:')
def exist_a_project(step):
    for project_hashes in step.hashes:
        mom = mommy.Mommy(Project, False)
        project = mom.make_one(name=project_hashes.get('name'), status=project_hashes.get('status'))
        
@step(u'exist a tool:')
def exist_a_tool(step):
    for tool_hashes in step.hashes:
        mom = mommy.Mommy(Tool, False)
        tool = mom.make_one(name=tool_hashes.get('name'), highlight=tool_hashes.get('highlight'))
