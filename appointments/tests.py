from django.test import TestCase
from patients.models import Patient
from providers.models import Provider
from django.contrib.auth.models import User
from .models import Appointment

class AppointmentModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='drsmith', first_name='John', last_name='Smith')
        self.provider = Provider.objects.create(user=self.user, specialty='Cardiology', phone='1234567890', address='123 Main St')
        self.patient = Patient.objects.create(name='John Doe')
        self.appointment = Appointment.objects.create(patient=self.patient, provider=self.provider, date='2023-10-10', time='10:00:00')

    def test_appointment_str(self):
        self.assertEqual(str(self.appointment), 'John Doe with Dr. Smith on 2023-10-10 at 10:00:00')