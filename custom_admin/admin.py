from django.contrib import admin
from .models import AdminModel

@admin.register(AdminModel)
class AdminModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')

# Customizing the admin interface
admin.site.site_header = "MyHealthApp Administration"
admin.site.site_title = "MyHealthApp Admin Portal"
admin.site.index_title = "Welcome to MyHealthApp Admin"