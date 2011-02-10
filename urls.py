from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^$', direct_to_template, {"template": 'index.html'}),

    (r'^history/$', 'apps.history.views.show'),
    (r'^projects/$', 'apps.projects.views.show_all'),
    (r'^teams/$', 'apps.teams.views.show_all'),
    (r'^member/(?P<member_id>\d+)$', 'apps.members.views.show'),


    (r'^site_media/(.*)$', 'django.views.static.serve', {"document_root": settings.MEDIA_ROOT}),
)
