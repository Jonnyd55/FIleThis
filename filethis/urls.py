from django.conf.urls import patterns, include, url
from django.contrib import admin
from cabinet.views import *

urlpatterns = patterns('',
    url(r'^$', 'cabinet.views.feed', name='user'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^catch/$', 'cabinet.views.catch_feed', name='catch_feed'),
    url(r'^button/$', 'cabinet.views.button', name='catch_button'),
    url(r'^search/$', 'cabinet.views.search', name='search'),
    url(r'^thanks/$', 'cabinet.views.thanks', name='thanks'),
    url(r'^feed/$', 'cabinet.views.feed', name='feed'),
    url(r'^account/$', 'cabinet.views.account', name='feed'),
    url(r'^tagged_item/(?P<tag>[-\w]+)/$', 'cabinet.views.tagged_items', name='search'),
    url('', include('social.apps.django_app.urls', namespace='social')),
)
