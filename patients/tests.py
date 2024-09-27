from django.test import TestCase
from .models import Patient

class PatientModelTest(TestCase):
    def setUp(self):
        self.patient = Patient.objects.create(name='John Doe', email='john@example.com', phone='1234567890')

    def test_patient_creation(self):
        self.assertEqual(self.patient.name, 'John Doe')
        self.assertEqual(self.patient.email, 'john@example.com')
        self.assertEqual(self.patient.phone, '1234567890')

    def test_patient_str(self):
        self.assertEqual(str(self.patient), 'John Doe')