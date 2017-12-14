'''
训练模型，包括训练方案，训练日志和动作库
'''
from django.db import models
from django.contrib.auth.models import User

class ExerciseType(models.Model):
    etype = models.CharField('动作类型', max_length=16)
    sort = models.CharField('动作类型细分', max_length=16)
    number = models.IntegerField('排序', default=0)

    def __str__(self):
        return self.etype + '-' + self.sort

    class Meta:
        ordering = ['number']
        verbose_name = '动作分类'
        verbose_name_plural = '动作分类'

class Exercise(models.Model):
    name = models.CharField('动作名', max_length=16)
    description = models.TextField('动作描述', blank=True)
    number = models.IntegerField('排序', default=0)
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
    name = models.CharField('方案名', max_length=16)
    description = models.TextField('方案说明', blank=True)
    ptype = models.ForeignKey(ProgramType, default=1, on_delete=models.SET_DEFAULT, verbose_name='方案类型')
    creator = models.ForeignKey(User, default=2, on_delete=models.SET_DEFAULT, verbose_name='创建者')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '训练方案'
        verbose_name_plural = '训练方案'

class TrainingDay(models.Model):
    day = models.IntegerField('天数', default=0)
    name = models.CharField('训练日', max_length=16)
    program = models.ForeignKey(Program, on_delete=models.CASCADE, verbose_name='训练方案')

    def __str__(self):
        return 'Day ' + str(self.day) + ':' + self.name

    class Meta:
        ordering = ['day']
        verbose_name = '训练日'
        verbose_name_plural = '训练日'

class TrainingSets(models.Model):
    number = models.IntegerField('排序', default=0)
    sets = models.IntegerField('组数', default=1)
    rest = models.IntegerField('组间歇', default=60)
    trainingday = models.ForeignKey(TrainingDay, on_delete=models.CASCADE,  verbose_name='训练日')

    def __str__(self):
        return 'Set ' + str(self.number)

    class Meta:
        abstract = True

class WeightSets(TrainingSets):
    minreps = models.IntegerField('最低次数', default=1)
    maxreps = models.IntegerField('最大次数', default=1)
    #动作数用于区别常规组与超级组，多余的动作当作备选动作
    enumber = models.IntegerField('动作数', default=1)
    exercises = models.ManyToManyField(Exercise, through='ExercisesInSets', verbose_name='动作列表')

    class Meta:
        ordering = ['number']
        verbose_name = '重量训练组'
        verbose_name_plural = '重量训练组'

class ExercisesInSets(models.Model):
    '重量训练组与动作的中间表'
    sets = models.ForeignKey(WeightSets, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    number = models.IntegerField('排序', default=0)

class PowerliftingSets(TrainingSets):
    reps = models.IntegerField('次数', default=1)
    load = models.FloatField('负重', default=1.0)
    exercise = models.ForeignKey(Exercise, on_delete=models.SET_DEFAULT, default=1, verbose_name='动作')

    class Meta:
        ordering = ['number']
        verbose_name = '力量训练组'
        verbose_name_plural = '力量训练组'










