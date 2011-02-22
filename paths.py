from lettuce.django import django_url


def path_to(page_name):
    return django_url(
        {
          'the history page': '/history',
          'the summary page': '/summary',
          'the projects page': '/projects',
          'the teams page': '/teams',
          'the page list all members': '/members',
          'the news page': '/news',
        }[page_name])

