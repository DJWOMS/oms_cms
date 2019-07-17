from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline

from oms_cms.backend.oms_seo.models import Seo


class SeoInlines(GenericStackedInline):
    """Seo"""
    model = Seo
    max_num = 1
