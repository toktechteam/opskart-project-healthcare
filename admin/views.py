from django.shortcuts import render
from .models import AdminModel

def admin_list(request):
    admins = AdminModel.objects.all()
    return render(request, 'admin/admin_list.html', {'admins': admins})