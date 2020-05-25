from django.conf import settings
from django.http import Http404, HttpResponsePermanentRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.utils.safestring import mark_safe
from django.views.decorators.csrf import csrf_protect
from django.utils.translation import get_language

from .models import Pages


def get_page(request, url):
    """Получение страницы по url"""
    if not url.startswith('/'):
        url = '/' + url

    if not request.LANGUAGE_CODE:
        language_code = settings.LANGUAGE_CODE
    else:
        language_code = get_language()

    language_prefix = '/%s' % language_code

    if url.startswith(language_prefix):
        url = url[len(language_prefix):]
    try:
        page = get_object_or_404(Pages, slug=url, lang=language_code, published=True)
    except Http404:
        if not url.endswith('/') and settings.APPEND_SLASH:
            url += '/'
            page = get_object_or_404(Pages, slug=url, lang=language_code, published=True)
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

    # if page.template:
    #     template = loader.get_template(page.template)
    # print(template)
    # # else:
    #     # template = loader.get_template(DEFAULT_TEMPLATE)
    # # t = Template(template)
    #
    # p = Template(template).render(RequestContext(request, {'page': page}))
    # print(p)
    # # page.title = mark_safe(page.title)
    # # page.text = mark_safe(page.text)
    # return HttpResponse(p)
    # # return HttpResponse(template.render({'page': page}, request))
    return render(request, page.template, {"page": page})
