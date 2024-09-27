from django.db import models
from patients.models import Patient
from providers.models import Provider

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f'{self.patient.name} with {self.provider} on {self.date} at {self.time}'