from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse
from urllib.parse import urlparse
from django.urls import resolve, reverse, translate_url
from django.utils.http import is_safe_url
from django.utils.translation import get_language, check_for_language
from django.views import View
from django.utils.translation import activate
# from oms_cms.backend.languages.context_processors import set_lang
from oms_cms.backend.languages.models import Lang
from urllib.parse import unquote
from django.utils.translation import (
    LANGUAGE_SESSION_KEY, check_for_language, get_language,
)


class GetLang(View):
    """Переключение языки"""
    def get(self, request):
        next = request.GET.get('next', request.META.get('HTTP_REFERER', ''))
        # if ((next or not request.is_ajax()) and
        #         not is_safe_url(url=next, allowed_hosts={request.get_host()}, require_https=request.is_secure())):
        #     next = request.META.get('HTTP_REFERER')
        #     next = next and unquote(next)  # HTTP_REFERER may be encoded.
        #     if not is_safe_url(url=next, allowed_hosts={request.get_host()}, require_https=request.is_secure()):
        #         next = '/'
        response = HttpResponseRedirect(next) if next else HttpResponse(status=204)
        if request.method == 'GET':
            lang_code = request.GET.get("language")
            if lang_code and check_for_language(lang_code):
                if next:
                    next_trans = translate_url(next, lang_code)
                    if next_trans != next:
                        response = HttpResponseRedirect(next_trans)
                if hasattr(request, 'session'):
                    request.session[LANGUAGE_SESSION_KEY] = lang_code
                response.set_cookie(
                    settings.LANGUAGE_COOKIE_NAME, lang_code,
                    max_age=settings.LANGUAGE_COOKIE_AGE,
                    path=settings.LANGUAGE_COOKIE_PATH,
                    domain=settings.LANGUAGE_COOKIE_DOMAIN,
                )
            activate(lang_code)
        return response
        # lang_code = request.GET.get('language', 'en')
        # print(lang_code)
        # lang = get_language()
        # print(lang)
        # print(request.get_host())
        # if not lang_code:
        #     lang_code = settings.LANGUAGE_CODE
        # next_url = request.META.get('HTTP_REFERER', '')
        # if not is_safe_url(next_url, request.get_host()):
        #     print("no next")
        #     next_url = '/'
        # print(next_url)
        # response = HttpResponseRedirect(next_url)
        # print(response)
        # if lang_code and check_for_language(lang_code):
        #     print("aaa")
        #     if hasattr(request, 'session'):
        #         request.session['django_language'] = lang_code
        #     response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang_code)
        #     activate(lang_code)
        # return response
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
        # return HttpResponseRedirect(reverse(url, kwargs=kwargs))

