from django.contrib import admin

from oms_cms.backend.languages.models import Lang
from oms_cms.backend.utils.models import EmailsFeedback


@admin.register(EmailsFeedback)
class EmailsFeedbackAdmin(admin.ModelAdmin):
    list_display = ("email", )


class MosesInline(admin.StackedInline):
    """Инлайн"""
    try:
        extra = Lang.objects.all().count()
        max_num = Lang.objects.all().count()
    except:
        pass

    template = 'admin/news/news.html'
    verbose_name = "Язык"
