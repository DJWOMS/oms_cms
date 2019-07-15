from django.http import HttpResponseRedirect
from urllib.parse import urlparse
from django.urls import resolve, reverse
from django.views import View

from oms_cms.backend.languages.context_processors import set_lang
from oms_cms.backend.languages.models import Lang


class GetLang(View):
    """Переключение языки"""
    def get(self, request, name):
        next = request.META['HTTP_REFERER']
        view, args, kwargs = resolve(urlparse(next)[2])
        # kwargs['request'] = request
        if not kwargs:
            url = "page_slug"
            kwargs['slug'] = name
        else:
            url = resolve(urlparse(next)[2]).url_name
            if url == "page_slug":
                if Lang.objects.filter(slug=kwargs['slug']).exists():
                    kwargs['slug'] = name
                else:
                    kwargs['lang'] = name
                if "lang" in kwargs:
                    url = "page_slug_lang"
                    kwargs['lang'] = name
            else:
                kwargs['lang'] = name
        request.session["lang"] = name
        return HttpResponseRedirect(reverse(url, kwargs=kwargs))

