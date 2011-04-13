from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    
    (r'^$', 'apps.home_page.views.show_index'),

    (r'^noticias/$', 'apps.news.views.show_news'),
    (r'^noticia/(?P<news_id>\d+)$', 'apps.news.views.detail_news'),
    
    (r'^passado/$', 'apps.nsi_info.views.show_history'),
    
    (r'^presente/$', 'apps.nsi_info.views.show_summary'),

    (r'^projetos/$', 'apps.projects.views.show_all'),
    (r'^projeto/(?P<project_id>\w+)/$', 'apps.projects.views.show_project'),

    (r'^membros/$', 'apps.members.views.show_all'),
    (r'^membro/(?P<member_id>\d+)$', 'apps.members.views.show'),

    (r'^ferramentas/$', 'apps.tools.views.show_all'),
    (r'^ferramenta/(?P<tool_id>\d+)$', 'apps.tools.views.show_tool'),
    
    (r'^site_media/(.*)$', 'django.views.static.serve', {"document_root": settings.MEDIA_ROOT}),
)
