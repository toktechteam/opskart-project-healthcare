from django.test import TestCase
from .models import Appointment
from patients.models import Patient
from providers.models import Provider

class AppointmentModelTest(TestCase):
    def setUp(self):
        self.patient = Patient.objects.create(name='John Doe', email='john@example.com', phone='1234567890')
        self.provider = Provider.objects.create(name='Dr. Smith', specialty='Cardiology')
        self.appointment = Appointment.objects.create(
            patient=self.patient,
            provider=self.provider,
            date='2023-10-10',
            time='10:00:00'
        )

    def test_appointment_creation(self):
        self.assertEqual(self.appointment.patient, self.patient)
        self.assertEqual(self.appointment.provider, self.provider)
        self.assertEqual(self.appointment.date, '2023-10-10')
        self.assertEqual(self.appointment.time, '10:00:00')

    def test_appointment_str(self):
        self.assertEqual(str(self.appointment), 'John Doe with Dr. Smith on 2023-10-10 at 10:00:00')