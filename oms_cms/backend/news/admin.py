from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from jet.admin import CompactInline

from .models import Post, Category, Tags, Comments


@admin.register(Category)
class CategoryAdmin(MPTTModelAdmin):
    """Категории"""
    list_display = ("name", "id",)
    list_display_links = ("name",)
    list_filter = ("name",)
    prepopulated_fields = {"slug": ("name",)}
    mptt_level_indent = 20


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    """Категории"""
    prepopulated_fields = {"slug": ("name",)}
    list_filter = ("name",)


class CommentsInline(CompactInline):
    model = Comments
    extra = 2
    show_change_link = True

    # readonly_fields = ('text',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Статьи"""
    list_display = ('title', 'created_date', 'get_category', 'lang', 'id')

    search_fields = ("title", "category", "lang")
    prepopulated_fields = {"slug": ("title",)}
    sortable_by = ("lang",)
    fieldsets = (
        (None, {
            'fields': (
                'author',
                'title',
                'subtitle',
                'mini_text',
                'text',
                'edit_date',
                'published_date',
                'photo',
                'gallery',
                'background_color',
                'category',
                'tag',
            )
        }),
        ('Настройки', {
            'classes': ('collapse',),
            'fields': (
                'lang',
                'template',
                'published',
                'status',
                'slug',
                'viewed',
            )
        }),
    )
    readonly_fields = ('viewed',)

    inlines = (CommentsInline,)

    def get_category(self, obj):
        return ",\n".join([p.name for p in obj.category.all()])

    get_category.short_description = "Категория"


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    """Коментарии к статьям"""
    list_display = ("user", "post", "date", "update")
    list_filter = ("user", "post", "date", "update")
