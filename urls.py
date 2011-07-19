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

    (r'^membros/$', 'apps.members.views.show_all'),
    (r'^membro/(?P<slug>[\w_-]+)$', 'apps.members.views.show'),

    (r'^ferramentas/$', 'apps.tools.views.show_all'),
    (r'^ferramenta/(?P<tool_slug>[\w_-]+)$', 'apps.tools.views.show_tool'),

    (r'^site_media/(.*)$', 'django.views.static.serve', {"document_root": settings.MEDIA_ROOT}),
)
