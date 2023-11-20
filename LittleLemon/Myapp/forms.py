from django import forms
from .models import Logger


class DateInput(forms.DateInput):
    input_type='date'

class DateTime(forms.DateTimeInput):
    input_type='time'

class Reservation(forms.ModelForm):
    class Meta:
        model=Logger
        fields=['name','email','phone_no','date','time','table']
        widgets = {
            'date': DateInput(),
            'time' : DateTime(),
        }
      