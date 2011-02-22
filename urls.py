from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^$', direct_to_template, {"template": 'index.html'}),

    (r'^news/$', 'apps.news.views.show_news'),
    (r'^history/$', 'apps.nsi_info.views.show_history'),
    (r'^summary/$', 'apps.nsi_info.views.show_summary'),

    (r'^projects/$', 'apps.projects.views.show_all'),
    (r'^projects/(?P<project_id>\w+)/$', 'apps.projects.views.show_project'),

    (r'^members/$', 'apps.members.views.show_all'),
    (r'^member/(?P<member_id>\d+)$', 'apps.members.views.show'),

    (r'^site_media/(.*)$', 'django.views.static.serve', {"document_root": settings.MEDIA_ROOT}),
)

