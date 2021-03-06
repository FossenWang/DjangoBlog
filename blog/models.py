from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.html import strip_tags
import markdown

# Create your models here.

class Category(models.Model):
    name = models.CharField('分类', max_length=16)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='分类'
        verbose_name_plural='分类'

class Topic(models.Model):
    name = models.CharField('话题', max_length=16)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='话题'
        verbose_name_plural='话题'

class Article(models.Model):
    '文章'
    title = models.CharField('标题', max_length=100)
    cover = models.ImageField(upload_to='blog/cover', blank=True, null=True, verbose_name='封面图')
    content = models.TextField('内容')
    pub_date = models.DateTimeField('发布日期')
    #作者与分类的默认值为2和1,代表着相应数据库中id的字段,分别手动将其设置为了unknown和uncategorized
    author = models.ForeignKey(User, default=2, on_delete=models.SET_DEFAULT, verbose_name='作者')
    category = models.ForeignKey(Category, default=1, on_delete=models.SET_DEFAULT, verbose_name='分类')
    topics = models.ManyToManyField(Topic, verbose_name='话题')
    views = models.PositiveIntegerField('阅读量', default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    class Meta:
        ordering=['-pub_date']
        verbose_name='文章'
        verbose_name_plural='文章'

class Comment(models.Model):
    content = models.CharField('评论', max_length=500)
    pub_date = models.DateTimeField('发布日期', auto_now_add=True)

    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='文章')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='评论人')
    
    def __str__(self):
        return self.content[:20]

    class Meta:
        verbose_name='评论'
        verbose_name_plural='评论'
