from lettuce.django import django_url


def path_to(page_name):
    return django_url(
        {
          'the NSI home page': '/', 
          'the history page': '/history',
          'the summary page': '/summary',
          'the projects page': '/projects',
          'the page list all members': '/members',
          'the news page': '/news',
          'the tools page': '/tools',
        }[page_name])

