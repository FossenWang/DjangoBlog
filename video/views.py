'''
视频推送相关的视图
'''
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView
from django.http import HttpResponseRedirect
from django.db.models.aggregates import Count

from .models import Video, Category, Tag

class HomeView(TemplateView):
    '首页视图'
    template_name = 'video/home.html'

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

class VideoDetailView(DetailView):
    '视频详情'
    model = Video
    template_name = 'video/video_detail.html'
    context_object_name = 'video'

class VideoListView(ListView):
    '视频列表'
    model = Video
    template_name = 'video/video_list.html'
    context_object_name = 'video_list'
    paginate_by = 30

    def get_queryset(self):
        if self.kwargs.get('number') == '0':
            return super().get_queryset()
        else:
            cate = get_object_or_404(Category, number=self.kwargs.get('number'))
            return super().get_queryset().filter(category=cate)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        paginator = context.get('paginator')
        page = context.get('page_obj')
        is_paginated = context.get('is_paginated')
        pagination_data = self.pagination_data(paginator, page, is_paginated)
        context.update(pagination_data)
        context['number'] = int(self.kwargs.get('number'))
        return context

    def pagination_data(self, paginator, page, is_paginated):
        '分页数据'
        if not is_paginated:
            return {}
        left = []
        right = []
        left_has_more = False
        right_has_more = False
        first = False
        last = False
        page_number = page.number
        total_pages = paginator.num_pages
        page_range = paginator.page_range

        if page_number == 1:
            right = page_range[page_number:page_number + 2]
            if right[-1] < total_pages - 1:
                right_has_more = True
            if right[-1] < total_pages:
                last = True

        elif page_number == total_pages:
            left = page_range[(page_number - 3) if (page_number - 3) > 0 else 0:page_number - 1]
            if left[0] > 2:
                left_has_more = True
            if left[0] > 1:
                first = True
        else:
            left = page_range[(page_number - 3) if (page_number - 3) > 0 else 0:page_number - 1]
            right = page_range[page_number:page_number + 2]
            if right[-1] < total_pages - 1:
                right_has_more = True
            if right[-1] < total_pages:
                last = True
            if left[0] > 2:
                left_has_more = True
            if left[0] > 1:
                first = True

        data = {
            'left': left,
            'right': right,
            'left_has_more': left_has_more,
            'right_has_more': right_has_more,
            'first': first,
            'last': last,
        }

        return data
