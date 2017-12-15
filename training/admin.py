from django.contrib import admin
from .models import ExerciseType, Exercise, ProgramType, Program, TrainingDay, WeightSets, PowerliftingSets

class WeightSetsInline(admin.TabularInline):
    model = WeightSets
    extra = 1

class PowerliftingSetsInline(admin.TabularInline):
    model = PowerliftingSets
    extra = 1

class TrainingDayInline(admin.TabularInline):
    model = TrainingDay
    extra = 1
    readonly_fields = ('admin_link', )

class TrainingDayAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'program')
    inlines = [WeightSetsInline, PowerliftingSetsInline]

class ProgramAdmin(admin.ModelAdmin):
    list_display = ('name', 'ptype')
    inlines = [TrainingDayInline]

class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('name', 'sort')


admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(Program, ProgramAdmin)
admin.site.register(TrainingDay, TrainingDayAdmin)
admin.site.register([ExerciseType, ProgramType, WeightSets, PowerliftingSets])
