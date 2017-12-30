from django.forms import ModelForm, HiddenInput

from .models import Program, TrainingDay, WeightSets, ExercisesInSets

class ProgramForm(ModelForm):
    class Meta:
        model = Program
        fields = ['name', 'cycle', 'ptype', 'creator', 'description']

class TrainingDayForm(ModelForm):
    class Meta:
        model = TrainingDay
        fields = ['day', 'name']
        widgets = {
            'day':HiddenInput,
        }
        

class WeightSetsForm(ModelForm):
    class Meta:
        model = WeightSets
        fields = ['number', 'minreps', 'maxreps', 'sets', 'rest']
        widgets = {
            'number':HiddenInput,
        }

class ExercisesInSetsForm(ModelForm):
    class Meta:
        model = ExercisesInSets
        fields = ['number', 'exercise']
