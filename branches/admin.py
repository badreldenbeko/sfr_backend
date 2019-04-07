from django.contrib import admin
from .models import Branch


class BranchAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name', 'branch_manager')


admin.site.register(Branch, BranchAdmin)
