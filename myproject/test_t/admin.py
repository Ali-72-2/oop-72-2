from django.contrib import admin
from .models import TestModel

@admin.register(TestModel)
class AdminTest(admin.ModelAdmin):
    list_display = ('name',)