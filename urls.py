from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),

    (r'^$', 'apps.home_page.views.show_index'),

    url(r'^', include('apps.news.urls')),

    (r'^sobre/$', 'apps.nsi_info.views.show_about'),

    url(r'^', include('apps.projects.urls')),

    url(r'^', include('apps.members.urls')),

    url(r'^', include('apps.tools.urls')),

    (r'^site_media/(.*)$', 'django.views.static.serve', {"document_root": settings.MEDIA_ROOT}),
)
