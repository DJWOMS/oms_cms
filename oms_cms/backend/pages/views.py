from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View

from .models import Pages


class Page(View):
    """Вывод страницы"""
    def get(self, request, slug=None):
        if slug is not None:
            page = get_object_or_404(Pages, slug=slug, activate=True)
        else:
            page = get_object_or_404(Pages, slug__isnull=True, activate=True)
        return render(request, page.template, {"page": page})
