from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    (r'^noticias/$', 'apps.news.views.show_news'),
    (r'^noticia/(?P<news_slug>[\w_-]+)$', 'apps.news.views.detail_news'),

)
