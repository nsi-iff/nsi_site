from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^nsi_site/', include('nsi_site.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
    (r'^project/new$', 'project.views.new_project'),
    (r'^project/update/(?P<project_name>[a-zA-Z- ]+)/$','project.views.update_project'),
    (r'^project/delete/(?P<project_name>[a-zA-Z- ]+)/$','project.views.delete_project')
)
