from django.contrib import admin
from .models import ExerciseType, Exercise, ProgramType, Program, TrainingDay, WeightSets, PowerliftingSets

class WeightSetsInline(admin.StackedInline):
    model = WeightSets
    extra = 1

class TrainingDayInline(admin.StackedInline):
    model = TrainingDay
    extra = 1
    inlines = [WeightSetsInline]

class ProgramAdmin(admin.ModelAdmin):
    list_display = ('name', )
    inlines = [TrainingDayInline]

class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('name', 'sort')


admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(Program, ProgramAdmin)
admin.site.register([ExerciseType, ProgramType, TrainingDay, WeightSets, PowerliftingSets])
