from django.conf.urls import patterns, include, url

from . import views

urlpatterns = patterns('',
    url(
    	r'^$',
    	view=views.PlayerListView.as_view(),
    	name='players',
	),
    url(
        r'^(?P<pk>\d+)/$',
        view=views.PlayerDetailView.as_view(),
        name='player_detail',
    ),
)
