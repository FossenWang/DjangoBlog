from django.conf.urls import url

from . import views

app_name = 'video'

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^video/(?P<pk>[0-9]+)/$', views.VideoDetailView.as_view(), name='video'),
    url(r'^video/category/(?P<number>[0-9]+)/$', views.VideoListView.as_view(), name='video list'),
    ]
