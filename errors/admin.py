from django.contrib import admin
from .models import ErrorGroup, Error


class ErrorInline(admin.StackedInline):
    model = Error


class ErrorGroupAdmin(admin.ModelAdmin):
    inlines = (ErrorInline,)


admin.site.register(ErrorGroup, ErrorGroupAdmin)
