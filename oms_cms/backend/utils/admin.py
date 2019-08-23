from django.contrib import admin

# from oms_cms.backend.languages.models import Lang
from oms_cms.backend.utils.models import EmailsFeedback


@admin.register(EmailsFeedback)
class EmailsFeedbackAdmin(admin.ModelAdmin):
    list_display = ("email", )


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


# class LangInline(admin.StackedInline):
#     """Инлайн"""
#     try:
#         extra = Lang.objects.all().count()
#         max_num = Lang.objects.all().count()
#     except:
#         pass
#
#     template = 'admin/news/news.html'
#     verbose_name = "Язык"
