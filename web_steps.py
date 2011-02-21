import datetime
from lettuce import world, step
from should_dsl import should, should_not
from paths import path_to


@step(r'I fill in "(.*)" with "(.*)"')
def fill_field(step, label, value):
    world.browser.fill_in(label, value)

@step(r'I go to "(.+)"')
def i_go_to(step, page_name):
    world.browser.visit(path_to(page_name))

@step(r'I press "(.*)"')
def press_button(step, name):
    world.browser.find_by_name(name.lower()).click()

@step(u'I click "(.*)"')
def i_click(step, link):
    world.browser.find_link_by_text(link).first.click()

@step(r'I should see "(.*)"$')
def i_should_see(step, content):
    world.browser.html |should| contain(content)

@step(u'I should have "(.*)" as HTML')
def i_should_have_as_html(step, html_output):
    # different step descriptions for intention-revealing purposes
    step.then('I should see "%s"' % html_output)

@step(u'I should see an image called "(.*)"')
def and_i_should_see_an_image_called_group1(step, image_name):
    images = world.browser.find_by_css_selector('img')
    found_image = [image for image in images if image['src'].endswith(image_name)]
    found_image |should| have_at_least(1).image

@step(u'I should see a link to "(.*)" with label "(.*)"')
def i_should_see_a_link_with_label(step, link_href, link_text):
    links = world.browser.find_link_by_text(link_text)
    links |should| have_at_least(1).item
    link = links[0]
    link['href'] |should| end_with(link_href)
