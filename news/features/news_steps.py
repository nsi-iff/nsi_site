import os
from lettuce import *
from nose.tools import assert_equals
from splinter.browser import Browser
from should_dsl import should
from django.conf import settings
from selenium.firefox.firefox_profile import FirefoxProfile
from news.models import News

@step('I have the following news')
def news_in_database(step):
    for news_dict in step.hashes:
        news = News(**news_dict)
        news.save()

@step(r'I am on the new news page')
def project_creation_page(step):
    world.browser.visit('http://localhost:8000/news/new')

@step(r'I am on the "(.*)" news edit page')
def news_update_page(step, news_title):
    news_title = news_title.replace(' ','%20')
    world.browser.visit('http://localhost:8000/news/update/'+news_title+'/')

@step(r'I am on the "(.*)" news delete page')
def news_delete_page(step, news_title):
    news_title = news_title.replace(' ','%20')
    world.browser.visit('http://localhost:8000/news/delete/'+news_title+'/')

@step(r'the "(.*)" news does not exist')
def news_does_not_exist(step, news_title):
    news = News.objects.filter(title=news_title)
    len(news) |should| equal_to(0)

@step(r'I attach to "(.*)" the "(.*)"')
def attach_file(step, label, value):
    value = os.path.join(
        settings.PROJECT_ROOT_PATH,
        'news/features/resources/'+value
    )
    world.browser.attach_file(label, value)

@before.each_scenario
def clear_images(scenario):
    images_dir = os.path.join(os.path.abspath('.'), 'site_media', 'images', 'news')
    print images_dir
    for image_file in os.listdir(images_dir):
        if image_file != '.' and image_file != '..':
            os.unlink(image_file)

