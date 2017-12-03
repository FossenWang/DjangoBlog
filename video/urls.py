from django.conf.urls import url

from . import views

app_name = 'video'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.VideoView.as_view(), name='video'),
    ]
