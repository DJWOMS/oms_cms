from django import forms
from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import InfoBlock


class InfoBlockAdminForm(forms.ModelForm):
    """Виджет редактора ckeditor"""
    desc = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = InfoBlock
        fields = '__all__'


@admin.register(InfoBlock)
class InfoBlockTitleAdmin(admin.ModelAdmin):
    """Бронирование"""
    list_display = ("title", "lang")
    search_fields = ("title",)
    list_filter = ("lang",)
    form = InfoBlockAdminForm
