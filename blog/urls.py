from django.conf.urls import re_path

from . import views

app_name = 'blog'

urlpatterns = [
    re_path(r'^$', views.HomeView.as_view(), name='home'),
    re_path(r'^index/$', views.IndexView.as_view(), name='index'),
    re_path(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    re_path(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.ArchivesView.as_view(), name='archives'),
    re_path(r'^category/(?P<name>.+)/$', views.CategoryView.as_view(), name='category'),
    re_path(r'^tag/(?P<pk>[0-9]+)/$', views.TagView.as_view(), name='tag'),
    re_path(r'^post/(?P<post_pk>[0-9]+)/comment/$', views.post_comment, name='post_comment'),
    re_path(r'^search/$', views.search, name='search'),
]