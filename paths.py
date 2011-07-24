from lettuce.django import django_url


def path_to(page_name):
    return django_url(
        {
          'the NSI home page': '/', 
          'the about page': '/sobre',
          'the projects page': '/projetos',
          'the page list all members': '/membros',
          'the news page': '/noticias',
          'the tools page': '/ferramentas',
          'the tool page': '/ferramenta',
          'page that list all former members': '/ex-membros',
        }[page_name])
