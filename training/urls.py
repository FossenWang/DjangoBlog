from django.conf.urls import url

from . import views

app_name = 'training'

urlpatterns = [
    url(r'^program/(?P<pk>[0-9]+)/$', views.ProgramDetailView.as_view(), name='program'),
    url(r'^program/(?P<pk>[0-9]+)/edit/$', views.EditProgramView.as_view(), name='edit program'),
    url(r'^program/category/(?P<pk>[0-9]+)/$', views.ProgramListView.as_view(), name='program list'),
    url(r'^exercise/category/(?P<number>[0-9]+)/$', views.ExerciseListView.as_view(), name='exercise list'),
    ]
