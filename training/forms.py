from django.forms import ModelForm, HiddenInput

from .models import Program, TrainingDay, WeightSets

class ProgramForm(ModelForm):
    class Meta:
        model = Program
        fields = ['name', 'cycle', 'ptype', 'description']
        widgets = {
            'creator':HiddenInput,
        }

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
        fields = ['number', 'exercises', 'minreps', 'maxreps', 'sets', 'rest']
        widgets = {
            'number':HiddenInput,
            'exercises':HiddenInput,
        }

