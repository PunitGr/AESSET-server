from django.conf.urls import url
from seating_manager import views


"""
Handles URL.
Views are mapped to a specific URL,
which runs when a request routes the URL to view.
"""

urlpatterns = [
    url(r'^studentlist/$', views.StudentListView.as_view()),
    url(r'^facultylist/$',
        views.FacultyListView.as_view()),
    url(r'^roomlist/$', views.RoomListView.as_view()),
    url(r'^subjectlist/$', views.SubjectListView.as_view()),
    url(r'^datesheet/$', views.DateSheetView.as_view())
]
