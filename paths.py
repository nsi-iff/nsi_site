from lettuce.django import django_url


def path_to(page_name):
    return django_url(
        {
          'the NSI home page': '/', 
          'the history page': '/passado',
          'the summary page': '/presente',
          'the projects page': '/projetos',
          'the page list all members': '/membros',
          'the news page': '/noticias',
          'the tools page': '/ferramentas',
          'the tool page': '/ferramenta',
        }[page_name])
