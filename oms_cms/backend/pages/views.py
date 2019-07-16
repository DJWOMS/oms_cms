from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View
from oms_cms.backend.languages.models import Lang

from .models import Pages


class Page(View):
    """Вывод страницы"""
    def get(self, request, lang=None, slug=None):
        if lang is None:
            lang = Lang.objects.get(is_default=True).slug
        if slug is not None:
            if Lang.objects.filter(slug=slug).exists():
                page = get_object_or_404(Pages, slug__isnull=True, lang__slug=slug, published=True)
            else:
                page = get_object_or_404(Pages, slug=slug, lang__slug=lang, published=True)
        else:
            page = get_object_or_404(Pages, slug__isnull=True, lang__slug=lang, published=True)
        return render(request, page.template, {"page": page})
