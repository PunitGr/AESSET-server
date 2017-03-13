from django.conf.urls import url
from query_management import views

"""
Handles URL.
Views are mapped to a specific URL,
which runs when a request routes the URL to view.
"""
urlpatterns = [
    url(r'^query/$', views.RequestQuery),
    url(r'^querylist/$', views.QueryList),
]
