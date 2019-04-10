from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'system', 'in_request')
    list_filter = ('system',)
    search_fields = ('name', 'code')


admin.site.register(Product, ProductAdmin)
