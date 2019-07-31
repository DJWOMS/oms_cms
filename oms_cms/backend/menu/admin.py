from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Menu, MenuItem
from .forms import MenuItemAdminForm


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    """Меню"""
    list_display = ("name", "status")


@admin.register(MenuItem)
class MenuItemAdmin(MPTTModelAdmin):
    """Пункты меню"""
    form = MenuItemAdminForm
    list_display = ("title", "name", "parent", "lang", "menu", "id")
    list_filter = ("menu", "parent", "lang")
    search_fields = ("name", "parent", "menu")
    save_as = True
    mptt_level_indent = 20

