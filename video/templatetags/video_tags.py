'模板标签'
from django import template
from ..models import Video, Category

register = template.Library()

@register.simple_tag
def get_recent_videos(num=4):
    '最近发布的视频'
    return Video.objects.all()[:num]

@register.simple_tag
def get_video_categories():
    return Category.objects.filter(number__gt=0).order_by('number')
