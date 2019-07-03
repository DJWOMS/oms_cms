from django.contrib import admin

from .models import InfoBlock, BlockField


class BlockFieldAdmin(admin.StackedInline):
    model = BlockField
    extra = 1
    show_change_link = True


@admin.register(InfoBlock)
class InfoBlockTitleAdmin(admin.ModelAdmin):
    """Бронирование"""
    list_display = ("title", "section")
    search_fields = ("title",)
    inlines = [BlockFieldAdmin]
