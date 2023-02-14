from django.contrib import admin
from .models import *

from import_export.admin import ExportActionMixin
from import_export.formats import base_formats

# Register your models here.

class StaffAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = (
        'first_name',
        'middle_name',
        'last_name',
        'date_of_birth',
        'designation',
        'job_title',
        'email',
        'mobile_number',
        'hometown',
        'lga',
        'state',
        'place_of_residence',
        'guarantor',
        'guarantor_phone',
        'guarantor_address',
        'attachment',
        'appointment_date',
    )
    list_filter = ('designation', 'job_title', 'attachment')
    search_fields = [
        'first_name',
        'middle_name',
        'last_name',
        'job_title',
        'designation',
    ]

    def get_export_formats(self):
        formats = (
            base_formats.XLS,
        )
        return [f for f in formats if f().can_export()]


class CustomerAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = (
        'first_name',
        'middle_name',
        'last_name',
        'email',
        'mobile_number',
        'place_of_residence',
    )
    search_fields = ['first_name', 'middle_name', 'last_name']

    def get_export_formats(self):
        formats = (
            base_formats.XLS,
        )
        return [f for f in formats if f().can_export()]


class UtilityAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('name', 'details')
    search_fields = ['name', 'details']

    def get_export_formats(self):
        formats = (
            base_formats.XLS,
        )
        return [f for f in formats if f().can_export()]


class AssetAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('name', 'details')
    search_fields = ['name', 'details']

    def get_export_formats(self):
        formats = (
            base_formats.XLS,
        )
        return [f for f in formats if f().can_export()]


admin.site.register(Staff, StaffAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Utility, UtilityAdmin)
admin.site.register(Asset, AssetAdmin)

admin.site.site_header = 'Simbi Gobal Resources Limited Admin'
admin.site.site_title = 'Admin'
