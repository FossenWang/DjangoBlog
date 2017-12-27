from django.conf.urls import url

from . import views

app_name = 'training'

urlpatterns = [
    url(r'^program/(?P<pk>[0-9]+)/$', views.ProgramDetailView.as_view(), name='program'),
    url(r'^program/(?P<pk>[0-9]+)/edit/$', views.EditProgramView.as_view(), name='edit_program'),
    url(r'^program/add/$', views.AddProgramView.as_view(), name='add_program'),
    url(r'^program/(?P<pk>[0-9]+)/delete/$', views.DeleteProgramView.as_view(), name='delete_program'),
    url(r'^program/category/(?P<pk>[0-9]+)/$', views.ProgramListView.as_view(), name='program_list'),
    url(r'^exercise/category/(?P<number>[0-9]+)/$', views.ExerciseListView.as_view(), name='exercise_list'),
    ]
