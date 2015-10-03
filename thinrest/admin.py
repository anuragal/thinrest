"""
admin.py for enabling admin functionality on models
"""
from django.contrib import admin

from .models import Employee, SystemSetting

admin.site.register(Employee)
admin.site.register(SystemSetting)