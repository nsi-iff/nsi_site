from lettuce import *
from nose.tools import assert_equals
from splinter.browser import Browser
from should_dsl import should
from project.models import Project

@step(r'I am on the new project page')
def project_creation_page(step):
    world.browser.visit('http://localhost:8000/project/new')

@step('I have the following project')
def project_in_database(step):
    for project_dict in step.hashes:
        project = Project(**project_dict)
        project.save()

@step(r'I am on the "(.*)" project edit page')
def project_update_page(step, project_name):
    project_name = project_name.replace(' ','%20')
    world.browser.visit('http://localhost:8000/project/update/'+project_name+'/')

@step(r'I am on the "(.*)" project delete page')
def project_delete_page(step, project_name):
    project_name = project_name.replace(' ','%20')
    world.browser.visit('http://localhost:8000/project/delete/'+project_name+'/')

@step(r'the "(.*)" project does not exist')
def project_does_not_exist(step, project_name):
    project = Project.objects.filter(name=project_name)
    len(project) |should| equal_to(0)

