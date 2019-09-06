from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import translate_url
from django.utils.http import is_safe_url
from django.views import View
from django.utils.translation import activate
from urllib.parse import unquote
from django.utils.translation import (
    LANGUAGE_SESSION_KEY, check_for_language,
)


class GetLang(View):
    """Переключение языков"""
    def check_lang(self, next_trans):
        if (next_trans.split("/")[3] == self.request.LANGUAGE_CODE) or (next_trans.split("/")[3] == ''):
            return True
        else:
            return False

    def get(self, request):
        next = request.GET.get('next', request.META.get('HTTP_REFERER', ''))
        if ((next or not request.is_ajax()) and
                not is_safe_url(url=next, allowed_hosts={request.get_host()}, require_https=request.is_secure())):
            next = request.META.get('HTTP_REFERER')
            next = next and unquote(next)  # HTTP_REFERER may be encoded.
            if not is_safe_url(url=next, allowed_hosts={request.get_host()}, require_https=request.is_secure()):
                next = '/'
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

