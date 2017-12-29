'训练相关视图'
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.forms import modelformset_factory, inlineformset_factory

from .models import Program, ProgramType, Exercise, ExerciseType, TrainingDay, WeightSets, ExercisesInSets
from .forms import ProgramForm, TrainingDayForm, WeightSetsForm, ExercisesInSetsForm

class ProgramListView(ListView):
    '训练方案列表'
    model = Program
    template_name = 'training/program_list.html'
    context_object_name = 'program_list'
    paginate_by = 10

    def get_queryset(self):
        if self.kwargs.get('pk') == '0':
            return super().get_queryset()
        else:
            ptype = get_object_or_404(ProgramType, pk=self.kwargs.get('pk'))
            return super().get_queryset().filter(ptype=ptype)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        paginator = context.get('paginator')
        page = context.get('page_obj')
        is_paginated = context.get('is_paginated')
        pagination_data = self.pagination_data(paginator, page, is_paginated)
        context.update(pagination_data)

        context['pk'] = int(self.kwargs.get('pk'))

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

class ProgramDetailView(DetailView):
    '视频详情'
    model = Program
    template_name = 'training/program_detail.html'
    context_object_name = 'program'

class ExerciseListView(ListView):
    '动作库'
    model = Exercise
    template_name = 'training/exercise_list.html'
    context_object_name = 'exercise_list'
    paginate_by = 10

    def get_queryset(self):
        if self.kwargs.get('number') == '0':
            return super().get_queryset()
        else:
            return super().get_queryset().filter(sort__number__startswith=self.kwargs.get('number'))

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

class EditProgramView(UpdateView):
    '编辑方案视图'
    model = Program
    context_object_name = 'program'
    template_name = 'training/program_edit.html'
    form_class = ProgramForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        TDFormSet = inlineformset_factory(Program, TrainingDay, form=TrainingDayForm, extra=0)
        WSFormSet = inlineformset_factory(TrainingDay, WeightSets, form=WeightSetsForm, fk_name='trainingday', extra=0)
        #EISFormSet = inlineformset_factory(WeightSets, ExercisesInSets, form=ExercisesInSetsForm, fk_name='sets', extra=0, can_delete=False)
        program = context['program']
        td_set = program.trainingday_set.all()
        if self.request.method == 'POST':
            wsformset_list = []
            tdformset = TDFormSet(self.request.POST, instance=program, prefix='day')
            for td in td_set:
                wsformset = WSFormSet(self.request.POST, instance=td, prefix='day-'+str(td.day-1)+'-sets')
                print(wsformset)
                wsformset_list.append(wsformset)
            context['tdformset'] = tdformset
            context['wsformset_list'] = wsformset_list
        else:
            td_list = []
            tdformset = TDFormSet(instance=program, prefix='day')
            i = 0
            for td, tdform in zip(td_set, tdformset):
                ws_list = []
                ws_set = td.weightsets_set.all()
                wsformset = WSFormSet(instance=td, prefix='day-'+str(i)+'-sets')
                i+=1
                for ws, wsform in zip(ws_set, wsformset):
                    if len(ws.exercises.all())>0:
                        ws_list.append([wsform, ws.exercises.all()[0]])
                    else:
                        ws_list.append([wsform, '暂未选择动作'])
                td_list.append([tdform, wsformset.management_form, ws_list, td.day-1])
            context['td_list'] = td_list
            context['td_management'] = tdformset.management_form
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        print(context)
        tdformset = context['tdformset']
        wsformset_list = context['wsformset_list']
        if tdformset.is_valid():
            tdformset.save()
        else:
            print(tdformset)
        for wsformset in wsformset_list:
            if wsformset.is_valid():
                ws=wsformset.save()
                print(ws)
            else:
                print(wsformset)
        return super().form_valid(form)

class AddProgramView(CreateView):
    '添加方案视图'
    model = Program
    context_object_name = 'program'
    template_name = 'training/program_add.html'
    form_class = ProgramForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        program = context['program']
        TDFormSet = inlineformset_factory(Program, TrainingDay, form=TrainingDayForm, extra=0)
        td_set = program.trainingday_set.all()
        if self.request.method == 'POST':
            tdformset = TDFormSet(self.request.POST, instance=program, prefix='day')
            context['tdformset'] = tdformset
        else:
            tdformset = TDFormSet(instance=program, prefix='day')
            context['td_management'] = tdformset.management_form
        return context

class DeleteProgramView(DeleteView):
    '删除方案视图'
    model = Program
    success_url = reverse_lazy('training:program_list', args=[0])
