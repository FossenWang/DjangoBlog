'训练相关视图'
from django.views.generic import ListView, DetailView

from .models import Program

class ProgramListView(ListView):
    '训练方案列表'
    model = Program
    template_name = 'training/program_list.html'
    context_object_name = 'program_list'

class ProgramDetailView(DetailView):
    '视频详情'
    model = Program
    template_name = 'training/program_detail.html'
    context_object_name = 'program'
