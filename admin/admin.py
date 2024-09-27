from django.contrib import admin
from .models import AdminModel

@admin.register(AdminModel)
class AdminModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')