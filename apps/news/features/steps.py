# -*- coding: utf-8 -*-
import os
import shutil
from lettuce import step, world
from datetime import datetime
from django.conf import settings
from lettuce.django import django_url
from model_mommy import mommy
from django.contrib.auth.models import User
from apps.projects.models import Project
from apps.news.models import News


@step(u'exist a author:')
def exist_a_author(step):
    for user in step.hashes:
        m = mommy.make_one(User, username=user.get('name'), email='a@a.com')

@step(u'exist a project:')
def exist_a_project(step):
    for project in step.hashes:
         m = mommy.make_one(Project, name=project.get('name'), logo=None)
                     
@step(u'the news "(.*)" is related with project "(.*)"')
def the_news_is_related_with_project(step, news_title, project_name):
    project_obj = Project.objects.get(name=project_name)
    news_obj = News.objects.get(title=news_title)
    news_obj.projects_relateds.add(project_obj)
    news_obj.save()
          
          
@step(u'exist a news:')
def exist_a_news(step):
    for news_hashes in step.hashes:
        author = User.objects.get(username__exact=news_hashes.get('author'))
        date, hour = news_hashes.get('datetime').split()
        day, month, year = date.split('/')
        hours, minutes = hour.split(':')
        date_time = datetime(int(year), int(month), int(day), int(hours), int(minutes))
        News(title=news_hashes.get('title'), summary=news_hashes.get('summary'), body=news_hashes.get('body'), image=news_hashes.get('image'), author=author, datetime=date_time).save()
        file_name = news_hashes.get('image').split('/')[-1]
        shutil.copy2(os.path.join(settings.PROJECT_ROOT_PATH, 'apps', 'news',
                                  'features', 'resources', file_name),
                     os.path.join(settings.MEDIA_ROOT, 'images', 'news'))
