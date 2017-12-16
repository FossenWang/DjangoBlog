from django.contrib import admin
from .models import ExerciseType, Exercise, ProgramType, Program, TrainingDay, WeightSets, PowerliftingSets, ExercisesInSets

class ExercisesInSetsInline(admin.TabularInline):
    model = ExercisesInSets
    extra = 1

class WeightSetsInline(admin.TabularInline):
    model = WeightSets
    extra = 0
    readonly_fields = ('admin_link', )
    #fields = ('number', 'sets', 'rest', 'exercises')

class PowerliftingSetsInline(admin.TabularInline):
    model = PowerliftingSets
    extra = 0

class TrainingDayInline(admin.TabularInline):
    model = TrainingDay
    extra = 1
    readonly_fields = ('admin_link', )

class WeightSetsAdmin(admin.ModelAdmin):
    inlines = [ExercisesInSetsInline]

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
admin.site.register(WeightSets, WeightSetsAdmin)
admin.site.register([ExerciseType, ProgramType, PowerliftingSets])
