from django import forms
from .models import People

class DataShiftForm(forms.ModelForm):
    class Meta:
        model = People
        fields = ('status_pool', 'class_in', 'class_out', 'office_in', 'office_out')
