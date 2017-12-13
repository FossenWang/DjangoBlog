'''
训练模型，包括训练方案，训练日志和动作库
'''
from django.db import models
from django.contrib.auth.models import User

class ExerciseType:
    etype = models.CharField('动作类型', maxlength=16)
    sort = models.CharField('动作类型细分', maxlength=16)
    number = models.IntegerField('排序', default=0)

    def __str__(self):
        return self.etype + '-' + self.sort

    class Meta:
        ordering = ['number']
        verbose_name = '动作分类'
        verbose_name_plural = '动作分类'

class Exercise(models.Model):
    name = models.CharField('动作名', maxlength=16)
    description = models.TextField('动作描述', blank=True)
    number = models.IntegerField('排序', default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['number']
        verbose_name = '动作'
        verbose_name_plural = '动作'

class Program(models.Model):
    name = models.CharField('方案名', maxlength=16)
    description = models.TextField('方案说明', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '训练方案'
        verbose_name_plural = '训练方案'

class TrainingDay(models.Nodel):
    name = models.CharField('训练日', maxlength=16)
    day = models.IntegerField('天数', default=0)











