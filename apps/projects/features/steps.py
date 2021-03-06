import os
import shutil
from django.conf import settings
from lettuce import step, world
from lettuce.django import django_url
from should_dsl import should
from model_mommy import mommy
from apps.members.models import Member
from apps.members.models import Participation
from apps.projects.models import Project, Document

@step(u'exist a project:')
def exist_a_project(step):
    for project in step.hashes:
        Project(**project).save()
        file_name = project['logo'].split('/')[-1]
        shutil.copy2(os.path.join(settings.PROJECT_ROOT_PATH, 'apps', 'projects',
                                'features', 'resources', file_name),
                   os.path.join(settings.MEDIA_ROOT, 'test', 'images', 'projects'))
                 
@step(u'exist a member:')
def exist_a_member(step):
    for member in step.hashes:
        mommy.make_one(Member, name=member.get('name'), site=None, lattes=None, photo=None)

@step(r'"(.*)" member started participation on "(.*)" project')
def member_started_participation_on_project(step, member_name, project_name):
    member_obj = Member.objects.get(name=member_name)
    project_obj = Project.objects.get(name=project_name)
    mommy.make_one(Participation, member=member_obj, project=project_obj)
    
@step(r'I go to the "(.+)" project page')
def i_go_to_project_page(step, project_name):
    project_obj = Project.objects.get(name=project_name)
    world.browser.visit(django_url('/projeto/%s' % project_obj.slug))

@step(u'"(.*)" project has attached the following documents:')
def project_has_attached_the_following_documents(step, project_name):
    project = Project.objects.get(name=project_name)
    document = Document(**step.hashes[0])
    document.project = project
    document.save()

@step(u'I should see a label "(.*)" with the link to "(.*)"')
def i_should_see_a_label_with_link(step, link_text, link_href):
    links = world.browser.find_link_by_href(link_href)
    links |should| have_at_least(1).item
    link_value = links[0].value
    link_value |should| equal_to(link_text)
