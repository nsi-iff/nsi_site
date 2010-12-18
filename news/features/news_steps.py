import os
from lettuce import *
from nose.tools import assert_equals
from splinter.browser import Browser
from should_dsl import should
from django.conf import settings
from news.models import News

@before.all
def set_browser():
    world.browser = Browser('zope.testbrowser')

@step(r'I am on the new news page')
def project_creation_page(step):
    world.browser.visit('http://localhost:8000/news/new')

@step(r'I fill in "(.*)" with "(.*)"')
def fill_field(step, label, value):
    world.browser.fill_in(label, value)

@step(r'I attach to "(.*)" the "(.*)"')
def attach_file(step, label, value):
    value = os.path.join(
        settings.PROJECT_ROOT_PATH,
        'news/features/resources/'+value
    )
    world.browser.attach_file(label, value)

@step(r'I press "(.*)"')
def press_button(step, name):
    world.browser.find_by_name(name.lower()).click()

@step(r'I should see "(.*)": "(.*)"')
def see_data_news(step, label, value):
    tag = world.browser.find_by_id(label.lower()).value
    result = "%s: %s" % (label, value)
    tag |should| equal_to(result)

@step('I have the following news')
def news_in_database(step):
    for news_dict in step.hashes:
        news = News(**news_dict)
        news.save()

@step(r'I am on the "(.*)" news edit page')
def news_update_page(step, news_title):
    news_title = news_title.replace(' ','%20')
    world.browser.visit('http://localhost:8000/news/update/'+news_title+'/')

@step(r'I am on the "(.*)" news delete page')
def news_delete_page(step, news_title):
    news_title = news_title.replace(' ','%20')
    world.browser.visit('http://localhost:8000/news/delete/'+news_title+'/')

@step(r'I should see the message "(.*)"')
def see_delete_news_message(step, value):
    tag = world.browser.find_by_css_selector('h1').value
    tag |should| equal_to(value)

@step(r'the "(.*)" news does not exist')
def news_does_not_exist(step, news_title):
    news = News.objects.filter(title=news_title)
    len(news) |should| equal_to(0)

@after.each_scenario
def clear_database(scenario):
    news = News.objects.all()
    for new in news:
        new.delete()

@after.all
def finish_him(total_result):
    world.browser.quit()
    print "Congratulations, %d of %d scenarios passed!" % (
        total_result.scenarios_passed,
        total_result.scenarios_ran
    )

