'模板标签'
from django import template
from ..models import Program, ProgramType, Exercise, ExerciseType
from django.db.models.aggregates import Count

register = template.Library()

@register.simple_tag
def get_program_types():
    '训练方案分类'
    return ProgramType.objects.annotate(counts=Count('program')).filter(counts__gt=0)

@register.simple_tag
def get_program_count():
    '训练方案总数'
    return Program.objects.all().count()

@register.simple_tag
def get_exercise_types():
    '动作分类'
    sorts = ExerciseType.objects.annotate(counts=Count('exercise')).filter(counts__gt=0)
    etypes = {}
    for sort in sorts:
        if sort.etype not in etypes.keys():
            etype_sorts = sorts.filter(etype=sort.etype)
            ecounts = sum([s.counts for s in etype_sorts])
            etypes[sort.etype] = [etype_sorts, sort.number//10, ecounts]
    return etypes

@register.simple_tag
def get_exercise_count():
    '动作总数'
    return Exercise.objects.all().count()
