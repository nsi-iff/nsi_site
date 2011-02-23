import os
import shutil
from lettuce import step, world
from django.conf import settings
from lettuce.django import django_url
from django.contrib.auth.models import User
from apps.projects.models import Project
from apps.news.models import News
from datetime import datetime


@step(u'exist a author "(.*)" with email "(.*)" and password "(.*)"')
def exist_a_author_with_email_and_password(step, name, email, password):
    User.objects.create_user(name, email, password).save()

@step(u'exist a project:')
def exist_a_project(step):
    for project in step.hashes:
        Project(**project).save()
        file_name = step.hashes[0]['logo'].split('/')[-1]
        shutil.copy2(os.path.join(settings.PROJECT_ROOT_PATH, 'apps', 'projects',
                                  'features', 'resources', file_name),
                     os.path.join(settings.MEDIA_ROOT, 'images', 'projects'))
                     
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
