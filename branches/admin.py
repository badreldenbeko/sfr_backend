from django.contrib import admin
from .models import Branch
from systems.models import System


class SystemInline(admin.StackedInline):
    model = System


class BranchAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name', 'branch_manager')
    inlines = (SystemInline,)


admin.site.register(Branch, BranchAdmin)
