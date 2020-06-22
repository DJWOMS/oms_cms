from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline

from oms_cms.backend.opengraph.models import OpenGraph


class OpenGraphInlines(GenericStackedInline):
    """OpenGraph inline"""
    model = OpenGraph
    max_num = 1
