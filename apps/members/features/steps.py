# -*- coding: utf-8 -*-
import os
import shutil
from lettuce import step, world
from django.conf import settings
from lettuce.django import django_url
from should_dsl import should
from apps.members.models import Member
from apps.members.models import Participation
from apps.projects.models import Project

@step(u'exist a project:')
def given_exist_a_project(step):
    for project in step.hashes:
        Project(**project).save()
        file_name = step.hashes[0]['logo'].split('/')[-1]
        shutil.copy2(os.path.join(settings.PROJECT_ROOT_PATH, 'apps', 'projects',
                                  'features', 'resources', file_name),
                     os.path.join(settings.MEDIA_ROOT, 'images', 'projects'))

@step(u'exist a member:')
def and_team_has_the_member(step):
    for member in step.hashes:
        Member(**member).save()

@step(r'"(.*)" member started participation the "(.*)" project in "(.*)"')
def and_member_participation_the_project_in(step, member_name, project_name, start_participation_date):
    member = Member.objects.get(name=member_name)
    project = Project.objects.get(name=project_name)
    Participation(member=member, project=project, start_date=start_participation_date).save()
    
@step(r'"(.*)" member participated on "(.*)" project between "(.*)" and "(.*)"')
def and_member_participated_on_project_between(step, member_name, project_name, start_participation_date, end_participation_date):
    member = Member.objects.get(name=member_name)
    project = Project.objects.get(name=project_name)
    Participation(member=member, project=project, start_date=start_participation_date, end_date=end_participation_date).save()    

@step(r'I go to the "(.+)" member page')
def i_go_to_member_page(step, member_name):
    member_obj = Member.objects.get(name=member_name)
    world.browser.visit(django_url('/member/%i' % member_obj.id))
    
@step(u'I should see a label "(.*)" with the link to "(.*)"')
def i_should_see_a_label_with_link(step, link_text, link_href):
    links = world.browser.find_link_by_href(link_href)
    links |should| have_at_least(1).item
    link = links[0]
    link['text'] |should| equal_to(link_text)
