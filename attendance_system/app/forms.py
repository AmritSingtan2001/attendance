from django import forms
from django.core.exceptions import ValidationError
from .models import Attendance
from django.utils import timezone

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['student', 'date', 'is_present']

    def __init__(self, *args, **kwargs):
        super(AttendanceForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['placeholder'] = f"Enter {field_name.capitalize()}"
            field.widget.attrs['class'] = 'form-control'
            field.required = True

            if field_name == 'is_present':
                field.widget = forms.CheckboxInput(attrs={'class': 'form-check-input'})
                field.label = "Is Present?"  
                
        self.fields['date'].widget = forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})

    def clean(self):
        cleaned_data = super().clean()
        student = cleaned_data.get('student')
        date = cleaned_data.get('date')

        if student and date:
            if Attendance.objects.filter(student=student, date=date).exists():
                raise ValidationError(f"{student} has already been marked present on {date}.")

        return cleaned_data
