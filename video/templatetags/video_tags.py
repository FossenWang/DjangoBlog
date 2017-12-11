'模板标签'
from django import template
from ..models import Video, Category
from django.db.models.aggregates import Count

register = template.Library()

@register.simple_tag
def get_recent_videos(num=4):
    '最近发布的视频'
    return Video.objects.all()[:num]

@register.simple_tag
def get_video_categories():
    '视频分类和分类下的视频数'
    return Category.objects.annotate(counts=Count('video')).filter(number__gt=0).order_by('number')

@register.simple_tag
def get_video_count():
    '视频总数'
    return Video.objects.all().count()
