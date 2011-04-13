import re
from lettuce import world, step
from should_dsl import should
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

# a "little" help from http://love-python.blogspot.com/2008/07/strip-html-tags-using-python.html
def remove_html_tags(data):
    p = re.compile(r'<.*?>')
    return p.sub('', data)

def remove_extra_spaces(data):
    p = re.compile(r'\s+')
    return p.sub(' ', data)

@step(r'I should see "(.*)"$')
def i_should_see(step, content):
    page_content = remove_extra_spaces(remove_html_tags(world.browser.html))
    page_content |should| contain(content)

@step(u'I should have "(.*)" as HTML')
def i_should_have_as_html(step, html_output):
    world.browser.html |should| contain(html_output)

@step(u'I should see an image called "(.*)"')
def and_i_should_see_an_image_called_group1(step, image_name):
    images = world.browser.find_by_css_selector('img')
    found_image = [image for image in images if image['src'].endswith(image_name)]
    found_image |should| have_at_least(1).image

@step(u'I should see a link to "(.*)" with label "(.*)"')
def i_should_see_a_link_to_with_label(step, link_href, link_text):
    links = world.browser.find_link_by_text(link_text)
    links |should| have_at_least(1).item
    link = links[0]
    link['href'] |should| end_with(link_href)

@step(u'I should see a link with text "(.*)"')
def i_should_see_a_link_with_text(step, link_text):
    world.browser.find_link_by_text(link_text) |should| have(1).item

