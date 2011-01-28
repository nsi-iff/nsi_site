from django.core.management import call_command
from selenium.firefox.firefox_profile import FirefoxProfile
from splinter.browser import Browser
from lettuce import after, before, world, step
from should_dsl import should
from paths import path_to

@before.all
def set_browser():
    enable_selenium_specs_to_run_offline()
    world.browser = Browser()

def enable_selenium_specs_to_run_offline():
    prefs = FirefoxProfile._get_webdriver_prefs()
    prefs['network.manage-offline-status'] = 'false'
    @staticmethod
    def prefs_func():
        return prefs
    FirefoxProfile._get_webdriver_prefs = prefs_func

@before.each_scenario
def clean_db(scenario):
   call_command('flush', interactive=False)
   call_command('loaddata', 'all')

@after.all
def finish_him(total_result):
    world.browser.quit()


# web steps
@step(r'I fill in "(.*)" with "(.*)"')
def fill_field(step, label, value):
    world.browser.fill_in(label, value)

@step(r'I go to (.+)')
def i_go_to(step, page_name):
    world.browser.visit(path_to(page_name))

@step(r'I press "(.*)"')
def press_button(step, name):
    world.browser.find_by_name(name.lower()).click()

@step(r'I should see "(.*)"')
def i_should_see(step, content):
    world.browser.html |should| contain(content)

