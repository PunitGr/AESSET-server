from django.conf.urls import url
from .views import *

"""
Handles URL.
Views are mapped to a specific URL,
which runs when a request routes the URL to view.
"""
urlpatterns = [
    url(r'^query/$', RequestQuery.as_view()),
    url(r'^querylist/$', QueryList.as_view()),
    url(r'^querylistform/$', QueryListFrom.as_view()),
    url(r'^queryupdate/(?P<token_id>[a-zA-Z0-9]+)/$',
        UpdateQueryView.as_view())
]
