from django.test import TestCase
from django.contrib.auth.models import User
from .models import Provider

class ProviderModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='drsmith', first_name='John', last_name='Smith')
        self.provider = Provider.objects.create(user=self.user, specialty='Cardiology', phone='1234567890', address='123 Main St')

    def test_provider_str(self):
        self.assertEqual(str(self.provider), 'Dr. Smith')