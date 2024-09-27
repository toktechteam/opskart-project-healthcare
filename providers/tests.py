from django.test import TestCase
from .models import Provider

class ProviderModelTest(TestCase):
    def setUp(self):
        self.provider = Provider.objects.create(name='Dr. Smith', specialty='Cardiology')

    def test_provider_creation(self):
        self.assertEqual(self.provider.name, 'Dr. Smith')
        self.assertEqual(self.provider.specialty, 'Cardiology')

    def test_provider_str(self):
        self.assertEqual(str(self.provider), 'Dr. Smith')