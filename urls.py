from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^$', direct_to_template, {"template": 'index.html'}),
    (r'^project/new$', 'project.views.new_project'),
    (r'^project/update/(?P<project_name>[a-zA-Z- ]+)/$','project.views.update_project'),
    (r'^project/delete/(?P<project_name>[a-zA-Z- ]+)/$','project.views.delete_project'),
    (r'^news/new$', 'news.views.new_news'),
    (r'^news/update/(?P<news_title>[a-zA-Z- ]+)/$','news.views.update_news'),
    (r'^news/delete/(?P<news_title>[a-zA-Z- ]+)/$','news.views.delete_news'),

    (r'^site_media/(.*)$', 'django.views.static.serve', {"document_root": settings.MEDIA_ROOT}),
)

