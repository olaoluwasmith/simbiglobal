from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ExportActionMixin
from import_export.formats import base_formats

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')


class ExpenseResource(resources.ModelResource):
    class Meta:
        model = Expenses
        fields = ('id', 'description', 'category_log__name', 'subcategory_log__name', 'amount', 'date')
        export_order = ('id', 'description', 'category_log__name', 'subcategory_log__name', 'amount', 'date')


class RevenueResource(resources.ModelResource):
    class Meta:
        model = Revenue
        fields = ('id', 'description', 'category_log__name', 'subcategory_log__name', 'amount', 'date')
        export_order = ('id', 'description', 'category_log__name', 'subcategory_log__name', 'amount', 'date')


class ExpenseAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('description', 'category_log', 'subcategory_log', 'amount', 'date')
    list_filter = (
        'date',
        'category_log',
        'subcategory_log',
    )
    search_fields = ['description', 'amount', 'date']
    resource_classes = [ExpenseResource]

    def get_export_formats(self):
        formats = (
            base_formats.XLS,
        )
        return [f for f in formats if f().can_export()]


class RevenueAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('description', 'category_log', 'subcategory_log', 'amount', 'date')
    list_filter = (
        'date',
        'category_log',
        'subcategory_log',
    )
    search_fields = ['description', 'amount', 'date']
    resource_classes = [RevenueResource]

    def get_export_formats(self):
        formats = (
            base_formats.XLS,
        )
        return [f for f in formats if f().can_export()]


admin.site.register(CategoryLog, CategoryAdmin)
admin.site.register(SubcategoryLog, SubcategoryAdmin)
admin.site.register(Expenses, ExpenseAdmin)
admin.site.register(Revenue, RevenueAdmin)
