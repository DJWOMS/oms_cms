from django.contrib import admin

from .models import Lang


@admin.register(Lang)
class LangAdmin(admin.ModelAdmin):
    """Языки"""
    list_display = ("name", "slug", "is_default")
    list_editable = ("is_default", )
    # prepopulated_fields = {"slug": ("name",)}
