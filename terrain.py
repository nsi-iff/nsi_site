import os
import time
from django.core.management import call_command
from django.conf import settings
from selenium.firefox.firefox_profile import FirefoxProfile
from splinter.browser import Browser
from lettuce import after, before, world
from web_steps import *

@before.harvest
def run_time(variables):
    world.before_all = time.time()

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
def clean_database(scenario):
    clean_data()
    clean_media()

def clean_data():
    call_command('flush', interactive=False)
    call_command('loaddata', 'all')

def clean_media():
    clean_media_by_kind('images')
    clean_media_by_kind('files')

def clean_media_by_kind(kind):
    images_dir = os.path.join(settings.MEDIA_ROOT, kind)
    for file_name in os.listdir(images_dir):
        clean_all(os.path.join(images_dir, file_name))

def clean_all(directory):
    for file_name in os.listdir(directory):
        absname = os.path.join(directory, file_name)
        if os.path.isdir(absname) and file_name not in ['.', '..']:
            clean_all(absname)
        elif not file_name.startswith('.'):
            os.unlink(absname)

@after.all
def finish_him(total_result):
    world.browser.quit()
    clean_media()
    
@after.harvest
def run_time(results):
    after_all = time.time()
    before_all = world.before_all
    result = int(after_all - before_all)
    minutes = result / 60
    seconds = result % 60
    features_ran = 0
    scenarios_ran = 0
    scenarios_passed = 0
    scenarios_failed = dict()
    for app in results:
        features_ran += app.features_ran
        scenarios_ran += app.scenarios_ran
        scenarios_passed += app.scenarios_passed
        for i in app.scenario_results:
            if i.passed == False:
                scenarios_failed.update({i.scenario.feature: i.scenario.name})

    print '-------------------------------------------------'
    print '%i features ran.' % features_ran
    print '%i scenarios ran.' % scenarios_ran
    print '%i scenarios passed.' % scenarios_passed
    if scenarios_failed:
        print 'Error in:'
        for scenario in scenarios_failed.iteritems():
            print scenario[0].name + ' ~> ' + scenario[1]
    else:
        print 'No errors! Congratulations!'
    print 'Everything ran in %i minute(s) and %i second(s).' % (minutes, seconds)
    print '-------------------------------------------------'
