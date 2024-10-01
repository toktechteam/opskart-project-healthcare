from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['patient', 'provider', 'date', 'time', 'reason', 'gender', 'age_group']  # Ensure new fields are included