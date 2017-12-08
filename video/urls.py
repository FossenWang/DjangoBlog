from django.conf.urls import url

from . import views

app_name = 'video'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^video/(?P<pk>[0-9]+)/$', views.VideoDetailView.as_view(), name='video'),
    url(r'^video/category/$', views.VideoListView.as_view(), name='video list'),
    #(?P<category>.+)/page=(?P<page>[0-9]+)
    ]
