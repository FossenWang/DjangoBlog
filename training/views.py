'训练相关视图'
import re
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.forms import modelformset_factory, inlineformset_factory

from .models import Program, ProgramType, Exercise, ExerciseType, TrainingDay, WeightSets
from .forms import ProgramForm, TrainingDayForm, WeightSetsForm

class ProgramCreatorTestMixin(UserPassesTestMixin):
    '验证发送请求的用户是否是方案创建者'
    def test_func(self):
        if self.request.user.is_authenticated:
            program = Program.objects.get(pk=self.kwargs.get('pk'))
            is_creator = self.request.user == program.creator
            self.raise_exception = not is_creator
        else:
            is_creator = False
        return is_creator

class ExerciseListView(ListView):
    '动作库'
    model = Exercise
    template_name = 'training/exercise_list.html'
    context_object_name = 'exercise_list'
    paginate_by = 30

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        program = context['program']
        td_list = []
        for td in program.trainingday_set.all():
            ws_list = []
            for ws in td.weightsets_set.all():
                exercises = [Exercise.objects.get(pk=pk) for pk in ws.exercises.split(',')]
                if exercises:
                    ws_list.append([ws, exercises])
                else:
                    ws_list.append([ws, {'name':'暂无'}])
            td_list.append([td, ws_list])
        context['td_list'] = td_list
        context['user_is_creator'] = self.request.user==program.creator
        return context

class EditProgramView(ProgramCreatorTestMixin, UpdateView):
    '编辑方案视图'
    model = Program
    context_object_name = 'program'
    template_name = 'training/program_edit.html'
    form_class = ProgramForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        program = context['program']
        TDFormSet = inlineformset_factory(Program, TrainingDay, form=TrainingDayForm, extra=0)
        if self.request.method == 'POST':
            tdformset = TDFormSet(self.request.POST, instance=program, prefix='day')
            context['tdformset'] = tdformset
        else:
            td_list = []
            tdformset = TDFormSet(instance=program, prefix='day')
            WSFormSet = inlineformset_factory(TrainingDay, WeightSets, form=WeightSetsForm, fk_name='trainingday', extra=0)
            for i, tdform in enumerate(tdformset):
                td = tdform.instance
                ws_list = []
                wsformset = WSFormSet(instance=td, prefix='day-'+str(i)+'-sets')
                for wsform in wsformset:
                    exercises = [Exercise.objects.get(pk=pk) for pk in wsform.instance.exercises.split(',')]
                    if exercises:
                        ws_list.append([wsform, exercises])
                    else:
                        ws_list.append([wsform, {'name':'暂无'}])
                td_list.append([tdform, wsformset.management_form, ws_list, i])
            context['td_list'] = td_list
            context['td_management'] = tdformset.management_form
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        post_dict = self.request.POST.copy()
        tdformset = context['tdformset']
        if tdformset.is_valid():
            tdformset.save()
            td_set = context['program'].trainingday_set.all()
            WSFormSet = modelformset_factory(WeightSets, form=WeightSetsForm, can_delete=True, extra=0)
            new_sets_keys = [
                'day-'+str(i)+'-sets-'+str(j)+'-trainingday' 
                for i in range(
                    int(post_dict['day-INITIAL_FORMS']), 
                    int(post_dict['day-TOTAL_FORMS']))
                for j in range(
                    int(post_dict['day-'+str(i)+'-sets-INITIAL_FORMS']), 
                    int(post_dict['day-'+str(i)+'-sets-TOTAL_FORMS']))]
            for key in new_sets_keys:
                if post_dict[key] == '-1':
                    day_key = re.sub('sets-([0-9]+)-trainingday$', 'day', key)
                    post_dict[key] = td_set[int(post_dict[day_key])-1].pk
            for i in range(len(tdformset)):
                wsformset = WSFormSet(post_dict, prefix='day-'+str(i)+'-sets')
                if wsformset.is_valid():
                    wsformset.save()
                else:
                    print(wsformset.errors)
        return super().form_valid(form)

class AddProgramView(LoginRequiredMixin, CreateView):
    '添加方案视图'
    model = Program
    context_object_name = 'program'
    template_name = 'training/program_add.html'
    form_class = ProgramForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.creator=self.request.user
        self.object.save()
        return HttpResponseRedirect(reverse('training:edit_program', args=[self.object.pk]))

class DeleteProgramView(ProgramCreatorTestMixin, DeleteView):
    '删除方案视图'
    model = Program
    success_url = reverse_lazy('training:program_list', args=[0])
