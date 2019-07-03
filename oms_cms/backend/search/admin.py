from django.contrib import admin

from .models import SpySearch


@admin.register(SpySearch)
class SpySearchAdmin(admin.ModelAdmin):
    """Счетчик поиска"""
    list_display = ("record", "counter")
