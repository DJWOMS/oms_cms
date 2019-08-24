from django.conf import settings
from django.http import HttpResponseRedirect
from urllib.parse import urlparse
from django.urls import resolve, reverse
from django.utils.http import is_safe_url
from django.utils.translation import get_language, check_for_language
from django.views import View

# from oms_cms.backend.languages.context_processors import set_lang
from oms_cms.backend.languages.models import Lang


class GetLang(View):
    """Переключение языки"""
    def get(self, request):
        from django.utils.translation import activate
        lang_code = request.GET.get('language', 'en')
        print(lang_code)
        lang = get_language()
        print(lang)
        print(request.get_host())
        if not lang_code:
            lang_code = request.GET.get('lang_code', settings.LANGUAGE_CODE)
        next_url = request.META.get('HTTP_REFERER', '')
        if not is_safe_url(next_url, request.get_host()):
            next_url = '/'
        response = HttpResponseRedirect(next_url)
        if lang_code and check_for_language(lang_code):
            if hasattr(request, 'session'):
                request.session['django_language'] = lang_code
            response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang_code)
            activate(lang_code)
        return response
        # next = request.META['HTTP_REFERER']
        # view, args, kwargs = resolve(urlparse(next)[2])
        # # kwargs['request'] = request
        # if not kwargs:
        #     url = "page_slug"
        #     kwargs['slug'] = name
        # else:
        #     url = resolve(urlparse(next)[2]).url_name
        #     if url == "page_slug":
        #         if Lang.objects.filter(slug=kwargs['slug']).exists():
        #             kwargs['slug'] = name
        #         else:
        #             kwargs['lang'] = name
        #         if "lang" in kwargs:
        #             url = "page_slug_lang"
        #             kwargs['lang'] = name
        #     else:
        #         kwargs['lang'] = name
        # request.session["lang"] = name
        return HttpResponseRedirect(reverse(url, kwargs=kwargs))

