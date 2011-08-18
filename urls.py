from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),

    (r'^$', 'apps.home_page.views.show_index'),

    (r'^noticias/$', 'apps.news.views.show_news'),
    (r'^noticia/(?P<news_slug>[\w_-]+)$', 'apps.news.views.detail_news'),

    (r'^sobre/$', 'apps.nsi_info.views.show_about'),

    (r'^projetos/$', 'apps.projects.views.show_all'),
    (r'^projeto/(?P<project_slug>[\w_-]+)/$', 'apps.projects.views.show_project'),

    (r'^membros/$', 'apps.members.views.show_all_current_members'),
    (r'^membro/(?P<slug>[\w_-]+)$', 'apps.members.views.show_member'),

    (r'^ex-membros/$', 'apps.members.views.show_all_former_members'),
    (r'^ex-membro/(?P<slug>[\w_-]+)$', 'apps.members.views.show_member'),

    (r'^ferramentas/$', 'apps.tools.views.show_all'),
    (r'^ferramenta/(?P<tool_slug>[\w_-]+)$', 'apps.tools.views.show_tool'),

    (r'^wiki/$', 'apps.wiki.views.show_all_wiki_items'),
    (r'^wiki/(?P<wiki_item_id>\d+)/$', 'apps.wiki.views.view_wiki_item'),
    (r'^wiki/novo_item/$', 'apps.wiki.views.add_wiki_item'),
    (r'^wiki/novo_item/adicionado_com_sucesso/$',
        direct_to_template, {'template': 'wiki_item_successfully_added.html'}),

    (r'^site_media/(.*)$', 'django.views.static.serve', {"document_root": settings.MEDIA_ROOT}),
)
