'''
视频推送模型
'''
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Category(models.Model):
    name = models.CharField('分类', max_length=16)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='分类'
        verbose_name_plural='分类'

class Tag(models.Model):
    name = models.CharField('标签', max_length=16)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='标签'
        verbose_name_plural='标签'

class Video(models.Model):
    '''
    作者与分类的默认值为2和1,代表着相应数据库中id字段,分别手动将其设置为了unknown和uncategorized
    '''
    title = models.CharField('标题', max_length=100)
    video = models.URLField('视频链接')
    video_length = models.CharField('视频时长', max_length=50, default='0:00')
    cover = models.ImageField(upload_to='video/cover', verbose_name='封面图')
    note = models.TextField('视频简介')
    pub_date = models.DateTimeField('发布日期')
    author = models.ForeignKey(User, default=2, on_delete=models.SET_DEFAULT, verbose_name='作者')
    category = models.ForeignKey(Category, default=1, on_delete=models.SET_DEFAULT, verbose_name='分类')
    tags = models.ManyToManyField(Tag, default=1, verbose_name='标签')
    views = models.PositiveIntegerField('播放量', default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    class Meta:
        ordering=['-pub_date']
        verbose_name='视频'
        verbose_name_plural='视频'
