from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline

from oms_cms.backend.oms_seo.models import Seo, ConnectSSModel


class SeoInlines(GenericStackedInline):
    """Seo inline"""
    model = Seo
    max_num = 1


@admin.register(ConnectSSModel)
class ConnectSSModelAdmin(admin.ModelAdmin):
    """Поисковые системы"""
    list_display = ("name",)