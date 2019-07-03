from django.http import HttpResponseRedirect
from urllib.parse import urlparse
from django.urls import resolve, reverse
from django.views import View

from oms_cms.backend.languages.context_processors import set_lang

class GetLang(View):
    """Переключение языки"""
    def get(self, request, name):
        next = request.META['HTTP_REFERER']
        view, args, kwargs = resolve(urlparse(next)[2])
        # kwargs['request'] = request
        kwargs['lang'] = name
        request.session["lang"] = name
        url = resolve(urlparse(next)[2]).url_name
        return HttpResponseRedirect(reverse(url, kwargs=kwargs))

