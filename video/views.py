'''
视频推送相关的视图
'''
from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponseRedirect

from .models import Video, Category, Tag


class IndexView(ListView):
    '首页视图'
    model = Video
    template_name = 'video/index.html'
    context_object_name = 'recent_video_list'
    #paginate_by = 10

    def get_context_data(self, **kwargs):
        '''
        覆盖该方法
        '''
        context = super().get_context_data(**kwargs)
        #paginator = context.get('paginator')
        #page = context.get('page_obj')
        #is_paginated = context.get('is_paginated')
        #pagination_data = self.pagination_data(paginator, page, is_paginated)
        #context.update(pagination_data)
        context['recent_video_list'] = Video.objects.all()[:4]
        return context

    '''
    def pagination_data(self, paginator, page, is_paginated):
        if not is_paginated:
            return {}

        left, right= [], []
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
        

    def upload_image(request):
    if request.method == 'POST':
        form = ModelFormWithFileField(request.POST, request.FILES)
        if form.is_valid():
            # file is saved
            form.save()
            return HttpResponseRedirect('/success/url/')
    else:
        form = ModelFormWithFileField()
    return render(request, 'upload.html', {'form': form})'''
