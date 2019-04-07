from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    search_fields = ['name', 'code', 'system']
    list_display = ('name', 'code', 'system', 'in_request')
    list_filter = ('system',)


admin.site.register(Product, ProductAdmin)
