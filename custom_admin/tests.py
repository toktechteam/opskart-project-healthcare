from django.test import TestCase
from django.contrib.admin.sites import AdminSite
from .models import AdminModel
from .admin import AdminModelAdmin

class AdminModelAdminTest(TestCase):
    def setUp(self):
        self.site = AdminSite()
        self.admin_model_admin = AdminModelAdmin(AdminModel, self.site)
        self.admin_model = AdminModel.objects.create(name='Admin Test')

    def test_admin_model_str(self):
        self.assertEqual(str(self.admin_model), 'Admin Test')