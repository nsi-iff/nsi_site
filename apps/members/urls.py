from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^membros/$', 'apps.members.views.show_all_current_members'),
    (r'^membro/(?P<slug>[\w_-]+)$', 'apps.members.views.show_member'),

    (r'^ex-membros/$', 'apps.members.views.show_all_former_members'),
    (r'^ex-membro/(?P<slug>[\w_-]+)$', 'apps.members.views.show_member'),

)
