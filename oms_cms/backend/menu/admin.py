from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from oms_cms.backend.utils.admin import ActionPublish
from .models import Menu, MenuItem
from .forms import MenuItemAdminForm


@admin.register(Menu)
class MenuAdmin(ActionPublish):
    """Меню"""
    list_display = ("name", "status", "published")
    list_filter = ("published",)
    actions = ['unpublish', 'publish']


@admin.register(MenuItem)
class MenuItemAdmin(MPTTModelAdmin, ActionPublish):
    """Пункты меню"""
    form = MenuItemAdminForm
    list_display = ("title", "name", "parent", "lang", "menu", "sort", "id", "published")
    list_filter = ("menu", "parent", "lang", "published")
    search_fields = ("name", "parent", "menu")
    save_as = True
    list_editable = ("sort", )
    mptt_level_indent = 20
    actions = ['unpublish', 'publish']

