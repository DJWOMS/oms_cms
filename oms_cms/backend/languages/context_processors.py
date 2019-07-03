# from django.core.context_processors import request

from .models import LangDefault


def set_lang(request):
    """Запись языка в сессию"""
    if request.session.get("lang") is None:
        request.session["lang"] = LangDefault.objects.first().lang_default.slug
    return {"lang": request.session.get("lang")}
