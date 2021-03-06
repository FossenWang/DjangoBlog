from django.conf.urls import url

from . import views

app_name = 'video'

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^(?P<pk>[0-9]+)/$', views.VideoDetailView.as_view(), name='video'),
    url(r'^category/(?P<number>[0-9]+)/$', views.VideoListView.as_view(), name='video list'),
    ]
