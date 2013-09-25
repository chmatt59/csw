from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'csw.views.home', name='home'),
    # url(r'^csw/', include('csw.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'qt.views.hp'),
    url(r'^backlog/$', 'qt.views.backlog'),
    url(r'^nc/$', 'qt.views.nonconformities'),
    url(r'^nc/add/$', 'qt.views.nc_add'),
    url(r'^nc/edit/(?P<nc_id>.*)/$', 'qt.views.nc_edit'),
    url(r'^nc/line/(?P<nc_id>.*)/$', 'qt.views.nc_line'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )
