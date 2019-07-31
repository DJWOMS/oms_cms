from django import forms
from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from oms_cms.backend.oms_seo.admin import SeoInlines
from .models import Post, Category, Tags, Comments


class ActionPublish(admin.ModelAdmin):
    """Action для публикации и снятия с публикации"""

    def unpublish(self, request, queryset):
        """Снять с публикации"""
        rows_updated = queryset.update(published=False)
        if rows_updated == 1:
            message_bit = "1 story was"
        else:
            message_bit = "%s stories were" % rows_updated
        self.message_user(request, "%s successfully marked as published." % message_bit)

    unpublish.short_description = "Снять с публикации"
    unpublish.allowed_permissions = ('change',)

    def publish(self, request, queryset):
        """Опубликовать"""
        rows_updated = queryset.update(published=True)
        if rows_updated == 1:
            message_bit = "1 story was"
        else:
            message_bit = "%s stories were" % rows_updated
        self.message_user(request, "%s successfully marked as published." % message_bit)

    publish.short_description = "Опубликовать"
    publish.allowed_permissions = ('change',)


class PostAdminForm(forms.ModelForm):
    """Виджет редактора ckeditor"""
    mini_text = forms.CharField(widget=CKEditorUploadingWidget())
    text = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'


class CommentAdminForm(forms.ModelForm):
    """Виджет редактора ckeditor"""
    text = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Comments
        fields = '__all__'


@admin.register(Category)
class CategoryAdmin(MPTTModelAdmin, ActionPublish):
    """Категории"""
    list_display = ("name", "slug", "published", "id")
    list_display_links = ("name",)
    list_filter = ("name", "published")
    list_editable = ("published",)
    prepopulated_fields = {"slug": ("name",)}
    mptt_level_indent = 20
    actions = ['unpublish', 'publish']
    inlines = (SeoInlines,)


@admin.register(Tags)
class TagsAdmin(ActionPublish):
    """Категории"""
    list_display = ("name", "published")
    list_filter = ("published",)
    list_editable = ("published",)
    prepopulated_fields = {"slug": ("name",)}
    actions = ['unpublish', 'publish']
    search_fields = ("name", )


class CommentsInline(admin.StackedInline):
    model = Comments
    extra = 1
    show_change_link = True


@admin.register(Post)
class PostAdmin(ActionPublish):
    """Статьи"""
    form = PostAdminForm
    list_display = ('title', 'lang', 'created_date', 'category', 'published', 'id')
    list_filter = ('lang', 'created_date', 'category', 'published')
    list_editable = ("published",)
    search_fields = ["title", "category", "tag"]
    prepopulated_fields = {"slug": ("title",)}
    actions = ['unpublish', 'publish']
    save_as = True
    autocomplete_fields = ["tag"]
    readonly_fields = ('viewed',)

    inlines = (SeoInlines, CommentsInline,)


@admin.register(Comments)
class CommentsAdmin(ActionPublish):
    """Коментарии к статьям"""
    list_display = ("user", "post", "date", "update", "published")
    list_filter = ("user", "post", "date", "update", "published")
    list_editable = ("published",)
    form = CommentAdminForm
    actions = ['unpublish', 'publish']
