from django import forms
from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import Contact, ContactSocNet, Feedback, ContactFields


class ContactAdminForm(forms.ModelForm):
    """Виджет редактора ckeditor"""
    description = forms.CharField(label="Описание", widget=CKEditorUploadingWidget(), required=False)

    class Meta:
        model = Contact
        fields = '__all__'


class SocialNetworksAdmin(admin.StackedInline):
    """Соц. сети"""
    model = ContactSocNet
    extra = 1
    show_change_link = True


class ContactFieldsAdmin(admin.StackedInline):
    """Соц. сети"""
    model = ContactFields
    extra = 1
    show_change_link = True


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """Контакты"""
    list_display = ("name", "id")
    search_fields = ("id",)
    inlines = (SocialNetworksAdmin, ContactFieldsAdmin)
    prepopulated_fields = {"slug": ("name",)}
    form = ContactAdminForm


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    """Обратная связь"""
    list_display = ("full_name", "email", "phone", "subject", "date", "id")
    search_fields = ("subject", "full_name", "email", "phone")
    list_filter = ("id", "subject", "full_name", "email", "phone")
