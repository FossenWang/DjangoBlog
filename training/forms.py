from django.forms import ModelForm

from .models import Program, TrainingDay, WeightSets, ExercisesInSets

class ProgramForm(ModelForm):
    class Meta:
        model = Program
        fields = ['name', 'cycle', 'ptype', 'creator', 'description']

class TrainingDayForm(ModelForm):
    class Meta:
        model = TrainingDay
        fields = ['day', 'name']

class WeightSetsForm(ModelForm):
    class Meta:
        model = WeightSets
        fields = [ 'minreps', 'maxreps', 'sets', 'rest']

class ExercisesInSetsForm(ModelForm):
    class Meta:
        model = ExercisesInSets
        fields = ['number', 'exercise']
