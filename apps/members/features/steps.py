# -*- coding: utf-8 -*-
import os
import shutil
from lettuce import step, world
from django.conf import settings
from lettuce.django import django_url
from apps.members.models import Member
from apps.members.models import Participation
from apps.projects.models import Project

@step(u'exist a project:')
def given_exist_a_project(step):
    Project(**step.hashes[0]).save()
    file_name = step.hashes[0]['logo'].split('/')[-1]
    shutil.copy2(os.path.join(settings.PROJECT_ROOT_PATH, 'apps', 'projects',
                              'features', 'resources', file_name),
                 os.path.join(settings.MEDIA_ROOT, 'images', 'projects'))

@step(u'exist a member:')
def and_team_has_the_member(step):
    Member(**step.hashes[0]).save()

@step(u'And "(.*)" member started participation the "(.*)" project in "(.*)"')
def and_member_participation_the_project_in(step, member_name, project_name, start_project_date):
    member = Member.objects.get(name=member_name)
    project = Project.objects.get(name=project_name)
    Participation(member=member, project=project, start_date=start_project_date).save()
    
@step(r'I go to the "(.+)" member page')
def i_go_to_member_page(step, member_name):
    member_obj = Member.objects.get(name=member_name)
    world.browser.visit(django_url('/member/%i' % member_obj.id))
