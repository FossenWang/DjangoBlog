'''
训练模型，包括训练方案，训练日志和动作库
'''
from django.db import models
from django.contrib.auth.models import User
from django.core import urlresolvers

class ExerciseType(models.Model):
    etype = models.CharField('动作类型', max_length=16)
    sort = models.CharField('动作类型细分', max_length=16)
    number = models.PositiveIntegerField('次序', default=0)

    def __str__(self):
        return self.etype + '-' + self.sort

    class Meta:
        ordering = ['number']
        verbose_name = '动作分类'
        verbose_name_plural = '动作分类'

class Exercise(models.Model):
    name = models.CharField('动作名', max_length=16)
    description = models.TextField('动作描述', blank=True)
    number = models.PositiveIntegerField('次序', default=0)
    sort = models.ForeignKey(ExerciseType, default=1, on_delete=models.SET_DEFAULT, verbose_name='分类')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['number']
        verbose_name = '动作'
        verbose_name_plural = '动作'

class ProgramType(models.Model):
    name = models.CharField('方案类型', max_length=16)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '方案类型'
        verbose_name_plural = '方案类型'

class Program(models.Model):
    name = models.CharField('方案名', max_length=48)
    description = models.TextField('方案说明', blank=True)
    cycle = models.PositiveIntegerField('周期', default=7)
    ptype = models.ForeignKey(ProgramType, default=1, on_delete=models.SET_DEFAULT, verbose_name='方案类型')
    creator = models.ForeignKey(User, default=2, on_delete=models.SET_DEFAULT, verbose_name='创建者')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '训练方案'
        verbose_name_plural = '训练方案'

class TrainingDay(models.Model):
    day = models.PositiveIntegerField('天数', default=0)
    name = models.CharField('名称', max_length=16)
    program = models.ForeignKey(Program, on_delete=models.CASCADE, verbose_name='训练方案')

    def admin_link(self):
        if self.pk:
            day_url = urlresolvers.reverse('admin:training_trainingday_change', args=(self.pk,))
            return u'<a href="%s" target="_blank">详情</a>' % day_url
        return u''
    admin_link.allow_tags = True
    admin_link.short_description = '详情'

    def __str__(self):
        return 'Day ' + str(self.day) + ':' + self.name

    class Meta:
        ordering = ['day']
        verbose_name = '训练日'
        verbose_name_plural = '训练日'

class TrainingSets(models.Model):
    number = models.PositiveIntegerField('次序', default=0)
    sets = models.PositiveIntegerField('组数', default=1)
    rest = models.PositiveIntegerField('组间歇(s)', default=60)
    trainingday = models.ForeignKey(TrainingDay, on_delete=models.CASCADE,  verbose_name='训练日')

    def __str__(self):
        return 'Set ' + str(self.number)

    class Meta:
        abstract = True

class WeightSets(TrainingSets):
    minreps = models.PositiveIntegerField('最低次数', default=1)
    maxreps = models.PositiveIntegerField('最大次数', default=1)
    #动作数用于区别常规组与超级组，多余的动作当作备选动作
    enumber = models.PositiveIntegerField('动作数', default=1)
    exercises = models.ManyToManyField(Exercise, through='ExercisesInSets')

    def admin_link(self):
        if self.pk:
            day_url = urlresolvers.reverse('admin:training_weightsets_change', args=(self.pk,))
            return u'<a href="%s" target="_blank">详情</a>' % day_url
        return u''
    admin_link.allow_tags = True
    admin_link.short_description = '详情'

    class Meta:
        ordering = ['number']
        verbose_name = '重量训练组'
        verbose_name_plural = '重量训练组'

class ExercisesInSets(models.Model):
    '重量训练组与动作的中间表'
    sets = models.ForeignKey(WeightSets, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, verbose_name='动作')
    number = models.PositiveIntegerField('次序', default=0)

    class Meta:
        ordering = ['number']
        verbose_name = '动作'
        verbose_name_plural = '动作列表'

class PowerliftingSets(TrainingSets):
    reps = models.PositiveIntegerField('次数', default=1)
    load = models.FloatField('负重(%1RM)', default=1.0)
    exercise = models.ForeignKey(Exercise, on_delete=models.SET_DEFAULT, default=1, verbose_name='动作')

    class Meta:
        ordering = ['number']
        verbose_name = '力量训练组'
        verbose_name_plural = '力量训练组'










