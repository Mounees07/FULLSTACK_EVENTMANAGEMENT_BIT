from django import forms
from .models import event_request

class EventRequestForm(forms.ModelForm):
   class Meta:
        model = event_request
        fields = '__all__'
        widgets = {
            'from_date': forms.DateInput(attrs={'type': 'date'}),
            'to_date': forms.DateInput(attrs={'type': 'date'}),
            'from_time': forms.TimeInput(attrs={'type': 'time'}),
            'to_time': forms.TimeInput(attrs={'type': 'time'}),
        }
