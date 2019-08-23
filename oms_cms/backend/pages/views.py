from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View
from oms_cms.backend.languages.models import Lang

from .models import Pages


class Page(View):
    """Вывод страницы"""
    def get(self, request, slug=None):
        if slug is not None:
            page = get_object_or_404(Pages, slug=slug, lang__slug=request.LANGUAGE_CODE, published=True)
        else:
            page = get_object_or_404(Pages, slug__isnull=True, lang__slug=request.LANGUAGE_CODE, published=True)
        return render(request, page.template, {"page": page})
