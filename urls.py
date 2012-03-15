from django.conf.urls.defaults import *
from django.views.generic.base import TemplateView
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),

    (r'^$', 'apps.home_page.views.show_index'),

    url(r'^', include('apps.news.urls')),

    (r'^sobre/$', 'apps.nsi_info.views.show_about'),

    url(r'^', include('apps.projects.urls')),

    url(r'^', include('apps.members.urls')),

    url(r'^', include('apps.tools.urls')),

    url(r"^opensource/$", TemplateView.as_view(template_name="opensource/index.html")),

    (r'^wiki/', include('apps.wiki.urls')),
)

urlpatterns += staticfiles_urlpatterns()
