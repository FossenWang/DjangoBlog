'''
视频推送相关的视图
'''
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.http import HttpResponseRedirect
from django.db.models.aggregates import Count

from .models import Video, Category, Tag


class IndexView(TemplateView):
    '首页视图'
    template_name = 'video/index.html'

    def get_context_data(self, **kwargs):
        '''
        获取首页展示的内容
        '''
        context = super().get_context_data(**kwargs)
        context['latest_video'] = Video.objects.all()[0]
        context['recent_videos'] = Video.objects.all()[1:5]
        cates = Category.objects.annotate(counts=Count('video')).filter(number__gt=0).filter(counts__gt=0).order_by('number')
        context['video_categories'] = [(Video.objects.filter(category__name=cate.name)[:4], cate) for cate in cates]
        return context

class VideoView(DetailView):
    '视频详情'
    model = Video
    template_name = 'video/video.html'
    context_object_name = 'video'
