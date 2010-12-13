from lettuce import *
from nose.tools import assert_equals
from splinter.browser import Browser
from should_dsl import should, should_not

@before.all
def set_browser():
    world.browser = Browser()
   
@step(r'I am on the new project page')
def project_page(step):
    world.browser.visit('http://localhost:8000/project/new')
    
@step(r'I fill in "(.*)" with "(.*)"')
def fill_field(step, label, value):
    world.browser.fill_in(label, value)
    
@step(r'I press "(.*)"')
def press_button(step, name):
    world.browser.find_by_name(name.lower()).click()
    
@step(r'I should see "(.*)": "(.*)"')
def see_data_project(step, label, value):
    tag = world.browser.find_by_name(label.lower()).value
    result = "%s: %s" % (label, value)
    tag |should| equal_to(result)
    
@after.all
def finish_him(total_result):
    world.browser.quit()
    print "Congratulations, %d of %d scenarios passed!" % (
        total_result.scenarios_passed,
        total_result.scenarios_ran
    )
