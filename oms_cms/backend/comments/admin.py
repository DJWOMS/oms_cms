from django.contrib import admin
from django import forms
from django.utils.translation import ugettext_lazy as _

from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.contrib.contenttypes.admin import GenericStackedInline

from oms_cms.backend.utils.admin import ActionPublish

from oms_cms.backend.comments.models import OmsComment


class CommentAdminForm(forms.ModelForm):
    """Виджет редактора ckeditor"""
    comment = forms.CharField(label=_("Комментарий"), widget=CKEditorUploadingWidget())

    class Meta:
        model = OmsComment
        fields = '__all__'
        exclude = ('is_public',)


@admin.register(OmsComment)
class CommentsAdmin(ActionPublish, admin.ModelAdmin):
    """Коментарии"""
    list_display = ("user", "user_name", "user_email", "submit_date", "update", "published", "is_removed")
    list_filter = ("submit_date", "update", "published", "is_removed")
    list_editable = ("published", "is_removed")
    search_fields = ("user", "user_name", "user_email", )
    actions = ['unpublish', 'publish']
    form = CommentAdminForm


class CommentsInlines(GenericStackedInline):
    """Comments inline"""
    model = OmsComment
    extra = 1
    show_change_link = True
    ct_field = "content_type"
    ct_fk_field = "object_pk"
    form = CommentAdminForm
