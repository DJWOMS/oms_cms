from django.contrib import admin

from .models import Video


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    """Видео"""
    list_display = ("title", "id")
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title",)
    fields = ("title", "link", "slug")
