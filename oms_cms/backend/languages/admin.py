from django.contrib import admin

from .models import LangDefault, Lang


@admin.register(LangDefault)
class ListLangAdmin(admin.ModelAdmin):
    """Язык по умолчанию"""
    list_display = ("lang_default",)


@admin.register(Lang)
class LangAdmin(admin.ModelAdmin):
    """Языки"""
    list_display = ("name", "slug")
    # prepopulated_fields = {"slug": ("name",)}
