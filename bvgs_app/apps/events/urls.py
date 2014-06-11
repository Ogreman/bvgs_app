from django.conf.urls import patterns, include, url

from . import views

urlpatterns = patterns('',
    url(
        r'^$',
        view=views.EventListView.as_view(),
        name='events',
    ),
    url(
        r'^(?P<pk>\d+)/$',
        view=views.EventDetailView.as_view(),
        name='event_detail',
    ),
)
