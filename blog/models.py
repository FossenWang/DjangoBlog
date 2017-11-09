from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    name = models.CharField('分类', max_length=16)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField('标签', max_length=16)

    def __str__(self):
        return self.name

class Post(models.Model):

    '''作者与分类的默认值为2和1,代表着相应数据库中id的字段,分别手动将其设置为了unknown和uncategorized'''

    title = models.CharField('标题', max_length=100)
    content = models.TextField('内容')
    excerpt = models.CharField('摘要', max_length=200, blank=True)
    pub_date = models.DateTimeField('发布日期')
    author = models.ForeignKey(User, default=2, on_delete=models.SET_DEFAULT, verbose_name='作者')
    category = models.ForeignKey(Category, default=1, on_delete=models.SET_DEFAULT, verbose_name='分类')
    tags = models.ManyToManyField(Tag, verbose_name='标签')
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

class Comment(models.Model):
    content = models.CharField('评论', max_length=500)
    pub_date = models.DateTimeField('发布日期')

    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='帖子')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='评论人')
    
    def __str__(self):
        return self.content