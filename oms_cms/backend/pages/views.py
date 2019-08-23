from django.conf import settings
from django.http import Http404, HttpResponsePermanentRedirect
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_protect

from .models import Pages


def get_page(request, url):
    """Получение страницы по url"""
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
            page = get_object_or_404(Pages, slug=url, lang__slug=request.LANGUAGE_CODE, published=True)
            return HttpResponsePermanentRedirect('%s/' % request.path)
        else:
            raise

    return render_page(request, page)


@csrf_protect
def render_page(request, page):
    """Рендер страницы"""
    if page.registration_required and not request.user.is_authenticated:
        from django.contrib.auth.views import redirect_to_login
        return redirect_to_login(request.path)
    return render(request, page.template, {"page": page})
