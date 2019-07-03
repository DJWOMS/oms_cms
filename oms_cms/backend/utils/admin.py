from django.contrib import admin

from jet.admin import CompactInline

from oms_cms.backend.languages.models import Lang


class MosesInline(CompactInline):
    """Инлайн"""
    try:
        extra = Lang.objects.all().count()
        max_num = Lang.objects.all().count()
    except:
        pass

    template = 'admin/news/news.html'
    verbose_name = "Язык"
