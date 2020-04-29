from django.contrib import admin
from checks.models import Printer, Check

# Register your models here.

@admin.register(Printer)
class PrinterAdmin(admin.ModelAdmin):
    fields = ['name', 'check_type']
    ordering = ['name', 'check_type']


@admin.register(Check)
class CheckAdmin(admin.ModelAdmin):
    fields = ['printer', 'check_type', 'status']
    ordering = ['printer', 'check_type', 'status']
