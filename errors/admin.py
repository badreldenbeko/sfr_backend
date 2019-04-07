from django.contrib import admin
from .models import ErrorGroup, Error


admin.site.register(ErrorGroup)
admin.site.register(Error)
