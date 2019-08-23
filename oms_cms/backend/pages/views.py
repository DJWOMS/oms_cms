from django.conf import settings
from django.http import Http404, HttpResponsePermanentRedirect
from django.shortcuts import render, get_object_or_404

from .models import Pages


def page(request, url):
    """Вывод страницы"""
    if not url.startswith('/'):
        url = '/' + url

    language_prefix = '/%s' % request.LANGUAGE_CODE

    if url.startswith(language_prefix):
        url = url[len(language_prefix):]

    try:
        page = get_object_or_404(Pages, slug=url, lang__slug=request.LANGUAGE_CODE, published=True)
    except Http404:
        if not url.endswith('/') and settings.APPEND_SLASH:
            url += '/'
            print("what?")
            page = get_object_or_404(Pages, slug=url, lang__slug=request.LANGUAGE_CODE, published=True)
            return HttpResponsePermanentRedirect('%s/' % request.path)
        else:
            raise
    return render(request, page.template, {"page": page})
