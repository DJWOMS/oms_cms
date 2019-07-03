from django.contrib import admin

from .models import AboutBlock


@admin.register(AboutBlock)
class AboutBlockAdmin(admin.ModelAdmin):
    """О нас"""
    list_display = ("title", )
    search_fields = ("title",)
