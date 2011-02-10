import os
from django.core.management import call_command
from django.contrib.auth.models import User
from django.conf import settings
from selenium.firefox.firefox_profile import FirefoxProfile
from splinter.browser import Browser
from lettuce import after, before, world
from web_steps import *


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
    create_admin()
    clean_images()


def clean_data():
    call_command('flush', interactive=False)
    call_command('loaddata', 'all')


def create_admin():
    User.objects.create_superuser('admin', 'admin@test.com', 'admin')


def clean_images():
    images_dir = os.path.join(settings.MEDIA_ROOT, 'images')
    clean_all(images_dir)


def clean_all(directory):
    for file_name in os.listdir(directory):
        absname = os.path.join(directory, file_name)
        if os.path.isdir(file_name) and file_name not in ['.', '..']:
            clean_all(absname)
        elif not file_name.startswith('.'):
            os.unlink(absname)


@after.all
def finish_him(total_result):
    world.browser.quit()
    clean_images()
