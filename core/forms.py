from django import forms

from core.models import Habit

# class BaseForm(forms.Form):
#     def __init__(self, *args, **kwargs):
#         kwargs.setdefault('label_suffix', '')  
#         super(BaseForm, self).__init__(*args, **kwargs)

# forms.Form = BaseForm

class HabitForm(forms.ModelForm):

    class Meta:
        model = Habit
        fields = ('goal',)
