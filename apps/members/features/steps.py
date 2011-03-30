# -*- coding: utf-8 -*-
import os
import shutil
from lettuce import step, world
from django.conf import settings
from lettuce.django import django_url
from should_dsl import should
from model_mommy import mommy
from apps.members.models import Member
from apps.members.models import Participation
from apps.projects.models import Project

@step(u'exist a project:')
def given_exist_a_project(step):
    for project in step.hashes:
        mommy.make_one(Project, name=project.get('name'), logo=None)

@step(u'exist a member:')
def exist_a_member(step):
    for member in step.hashes:
        Member(**member).save()
        file_name = member.get('photo').split('/')[-1]
        shutil.copy2(os.path.join(settings.PROJECT_ROOT_PATH, 'apps', 'members',
                                  'features', 'resources', file_name),
                     os.path.join(settings.MEDIA_ROOT, 'test', 'images', 'members'))

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
    world.browser.visit(django_url('/membro/%i' % member_obj.id))
    
@step(u'I should see a label "(.*)" with the link to "(.*)"')
def i_should_see_a_label_with_link(step, link_text, link_href):
    links = world.browser.find_link_by_href(link_href)
    links |should| have_at_least(1).item
    link = links[0]
    link['text'] |should| equal_to(link_text)
 
@step(r'I should see the following members')
def i_should_see_the_following_members(step):
    
    for member_data in step.hashes:
        member = Member.objects.get(name=member_data['name'])
        
        container_photo = world.browser.find_by_css_selector('#member%s .avatar' % member.id)
        container_image_name = container_photo[0]['src'].split("/")[-1]
        container_image_name |should| equal_to(member_data['photo'])
        
        title_text = world.browser.find_by_css_selector('#member%s h1' % member.id)
        title_text[0].value |should| equal_to(member_data['name'])
        
        function_text = world.browser.find_by_css_selector('#member%s span' % member.id)
        function_text[0].value |should| equal_to(member_data['function'])
        
        currently_does_text = world.browser.find_by_css_selector('#member%s p' % member.id)
        currently_does_text[0].value |should| equal_to(member_data['currently_does'])
        
        container_links = world.browser.find_by_css_selector('#member%s .links a' % member.id)
        container_links_href = [x['href'] for x in container_links]
        
        member_data['site'] |should| be_into(container_links_href)
        member_data['github'] |should| be_into(container_links_href)
        member_data['twitter'] |should| be_into(container_links_href)
        member_data['slideshare'] |should| be_into(container_links_href)
