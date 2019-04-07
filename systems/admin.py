from django.contrib import admin
from .models import System


class SystemAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name', 'branch')
    list_filter = ('branch',)


admin.site.register(System, SystemAdmin)
