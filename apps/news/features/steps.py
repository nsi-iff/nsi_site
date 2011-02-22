from lettuce import step, world
from django.contrib.auth.models import User
from apps.projects.models import Project
from apps.news.models import New
from datetime import datetime


@step(u'exist a author "(.*)" with email "(.*)" and password "(.*)"')
def exist_a_author_with_email_and_password(step, name, email, password):
    User.objects.create_user(name, email, password).save()
    
@step(u'exist a project:')
def exist_a_project(step):
    Project(**step.hashes[0]).save()

@step(u'And exist a new with title "(.*)", summary "(.*)", body "(.*)", image "(.*)", author "(.*)", date and time "(.*)" and project "(.*)"')
def exist_a_new_with_title_summary_body_image_author_date_time_and_project(step, title, summary, body, image, author, date_time, project):
    author = User.objects.get(username__exact=author)
    project = Project.objects.get(name=project)
    date, hour = date_time.split()
    day, month, year = date.split('/')
    hours, minutes = hour.split(':')
    date_time = datetime(int(year), int(month), int(day), int(hours), int(minutes))
    New.objects.create(title=title, summary=summary, body=body, image=image, author=author, datetime=date_time, project=project)

