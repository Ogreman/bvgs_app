from django.conf.urls import patterns, include, url

from . import views

urlpatterns = patterns('',
    url(
    	r'^$',
    	view=views.PlayerListView.as_view(),
    	name='home',
	),
)
