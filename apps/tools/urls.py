from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    (r'^ferramentas/$', 'apps.tools.views.show_all'),
    (r'^ferramenta/(?P<tool_slug>[\w_-]+)$', 'apps.tools.views.show_tool'),

)
