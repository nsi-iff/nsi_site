from lettuce import *
from nose.tools import assert_equals
from splinter.browser import Browser
from should_dsl import should
from project.models import Project

@before.all
def set_browser():
    world.browser = Browser()

@step(r'I am on the new project page')
def project_creation_page(step):
    world.browser.visit('http://localhost:8000/project/new')

@step(r'I fill in "(.*)" with "(.*)"')
def fill_field(step, label, value):
    world.browser.fill_in(label, value)

@step(r'I press "(.*)"')
def press_button(step, name):
    world.browser.find_by_name(name.lower()).click()

@step(r'I should see "(.*)": "(.*)"')
def see_data_project(step, label, value):
    tag = world.browser.find_by_id(label.lower()).value
    result = "%s: %s" % (label, value)
    tag |should| equal_to(result)

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

@step(r'I should see the message "(.*)"')
def see_delete_project_message(step, value):
    tag = world.browser.find_by_css_selector('h1').value
    tag |should| equal_to(value)

@step(r'the "(.*)" project does not exist')
def project_does_not_exist(step, project_name):
    project = Project.objects.filter(name=project_name)
    len(project) |should| equal_to(0)

@after.each_scenario
def clear_database(scenario):
    projects = Project.objects.all()
    for project in projects:
        project.delete()

@after.all
def finish_him(total_result):
    world.browser.quit()
    print "Congratulations, %d of %d scenarios passed!" % (
        total_result.scenarios_passed,
        total_result.scenarios_ran
    )

