from django import forms
from django.contrib import admin, messages
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _
from mptt.admin import MPTTModelAdmin
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from oms_cms.backend.oms_seo.admin import SeoInlines
from oms_cms.backend.comments.admin import CommentsInlines
from oms_cms.backend.utils.admin import ActionPublish

from .models import Post, Category, Tags, FilterPost


class PostAdminForm(forms.ModelForm):
    """Виджет редактора ckeditor"""
    mini_text = forms.CharField(label="Превью статьи", widget=CKEditorUploadingWidget())
    text = forms.CharField(label="Полная статья", widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'


class CategoryAdminForm(forms.ModelForm):
    """Виджет редактора ckeditor"""
    description = forms.CharField(label="Описание", widget=CKEditorUploadingWidget(),
                                  required=False)

    class Meta:
        model = Category
        fields = '__all__'


@admin.register(Category)
class CategoryAdmin(MPTTModelAdmin, ActionPublish):
    """Категории"""
    list_display = ("name", "slug", "lang", "published", "sort", "id")
    list_display_links = ("name",)
    list_filter = ("name", "published")
    list_editable = ("published", "sort")
    prepopulated_fields = {"slug": ("name",)}
    mptt_level_indent = 20
    actions = ['unpublish', 'publish']
    inlines = (SeoInlines,)
    form = CategoryAdminForm
    readonly_fields = ("get_slug_url",)

    def save_model(self, request, obj, form, change):
        messages.add_message(request, messages.INFO, 'Hello world.')
        obj.save()


@admin.register(Tags)
class TagsAdmin(ActionPublish):
    """Теги статей"""
    list_display = ("name", "published")
    list_filter = ("published",)
    list_editable = ("published",)
    prepopulated_fields = {"slug": ("name",)}
    actions = ['unpublish', 'publish']
    search_fields = ("name",)


@admin.register(FilterPost)
class FilterPostAdmin(ActionPublish):
    """Filter post"""
    list_display = ("title", "name", "published", "get_image")
    list_filter = ("published",)
    list_editable = ("published",)
    actions = ['unpublish', 'publish']
    search_fields = ("name",)

    def get_image(self, obj):
        if obj.icon:
            return mark_safe(
                f'<img src="{obj.icon.url}" width="50" height=50 />'
            )

    get_image.short_description = _("Иконка")


@admin.register(Post)
class PostAdmin(ActionPublish):
    """Статьи"""
    form = PostAdminForm
    list_display = (
        'title', 'lang', 'created_date', 'edit_date', 'published_date',
        'category', 'published', "sort", 'id'
    )
    list_filter = ('lang', 'created_date', 'category', 'published')
    list_editable = ("published", "sort")
    search_fields = ["title", "category", "tag"]
    prepopulated_fields = {"slug": ("title",)}
    actions = ['unpublish', 'publish']
    save_as = True
    save_on_top = True
    autocomplete_fields = ["tag"]
    readonly_fields = ('viewed', "get_slug_url")
    inlines = (SeoInlines, CommentsInlines,)
