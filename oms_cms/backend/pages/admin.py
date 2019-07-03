from django.contrib import admin

from .models import Pages


@admin.register(Pages)
class PagesAdmin(admin.ModelAdmin):
    """Статичные страницы"""
    list_display = ("title", "activate", "lang", "id")
    list_editable = ("activate", )
    list_filter = ("author", "activate", "template", "lang")
    search_fields = ("title", "lang")
    prepopulated_fields = {"slug": ("title", )}




