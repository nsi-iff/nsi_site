import os
import shutil
from datetime import datetime
from django.conf import settings
from lettuce import step, world
from lettuce.django import django_url
from model_mommy import mommy
from apps.members.models import Member
from apps.members.models import Participation
from apps.projects.models import Project, Document

@step(u'exist a project:')
def exist_a_project(step):
    for project in step.hashes:
        Project(**project).save()
        file_name = step.hashes[0]['logo'].split('/')[-1]
        shutil.copy2(os.path.join(settings.PROJECT_ROOT_PATH, 'apps', 'projects',
                                'features', 'resources', file_name),
                   os.path.join(settings.MEDIA_ROOT, 'images', 'projects'))
                 
@step(u'exist a member:')
def exist_a_member(step):
    for member in step.hashes:
        m = mommy.make_one(Member, name=member.get('name'), site=None, lattes=None, photo=None)

@step(r'"(.*)" member started participation on "(.*)" project')
def member_started_participation_on_project(step, member_name, project_name):
    member_obj = Member.objects.get(name=member_name)
    project_obj = Project.objects.get(name=project_name)
    mommy.make_one(Participation, member=member_obj, project=project_obj)
    
@step(r'I go to the "(.+)" project page')
def i_go_to_project_page(step, project_name):
    project_obj = Project.objects.get(name=project_name)
    world.browser.visit(django_url('/projects/%i' % project_obj.id))

@step(u'"(.*)" project has attached the following documents:')
def project_has_attached_the_following_documents(step, project_name):
    project = Project.objects.get(name=project_name)
    document = Document(**step.hashes[0])
    document.project = project
    document.save()

