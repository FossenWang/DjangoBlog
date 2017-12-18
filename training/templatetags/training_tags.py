'模板标签'
from django import template
from ..models import Program, ProgramType
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
