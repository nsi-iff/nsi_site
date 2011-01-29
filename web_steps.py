from lettuce import world, step
from should_dsl import should
from paths import path_to

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

@step(u'I should have "(.*)" as HTML')
def i_should_have_as_html(step, html_output):
    # different step descriptions for intention-revealing purposes
    step.then('I should see "%s"' % html_output)

