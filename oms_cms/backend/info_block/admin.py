from django import forms
from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import InfoBlock, BlockField


class InfoBlockAdminForm(forms.ModelForm):
    """Виджет редактора ckeditor"""
    desc = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = InfoBlock
        fields = '__all__'


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
    form = InfoBlockAdminForm
