from django.conf.urls import re_path

from . import views

app_name = 'blog'

urlpatterns = [
    re_path(r'^$', views.HomeView.as_view(), name='home'),
    re_path(r'^article/(?P<pk>[0-9]+)/$', views.ArticleDetailView.as_view(), name='detail'),
    re_path(r'^category/(?P<category_pk>[0-9]+)/$', views.CategoryView.as_view(), name='category'),
    re_path(r'^topic/(?P<topic_pk>[0-9]+)/$', views.TopicView.as_view(), name='topic'),
    re_path(r'^article/(?P<article_pk>[0-9]+)/comment/$', views.article_comment, name='article-comment'),
    re_path(r'^search/$', views.search, name='search'),
]