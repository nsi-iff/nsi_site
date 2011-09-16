from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    (r'^projetos/$', 'apps.projects.views.show_all'),
    (r'^projeto/(?P<project_slug>[\w_-]+)/$', 'apps.projects.views.show_project'),

)
