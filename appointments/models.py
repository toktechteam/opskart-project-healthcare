from django.db import models
from patients.models import Patient
from providers.models import Provider

class Appointment(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    AGE_GROUP_CHOICES = [
        ('A', 'Adult'),
        ('K', 'Kid'),
    ]

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    reason = models.TextField()  # Add this field
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)  # Add this field
    age_group = models.CharField(max_length=1, choices=AGE_GROUP_CHOICES, default='A')  # Default to 'Adult'

    def __str__(self):
        return f'{self.patient.name} with {self.provider} on {self.date} at {self.time}'