from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^players/', include('bvgs_app.apps.players.urls')),
    url(r'^events/', include('bvgs_app.apps.events.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
