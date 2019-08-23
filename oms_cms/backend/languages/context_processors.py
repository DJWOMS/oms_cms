# from django.core.context_processors import request

# from .models import Lang
#
#
# def set_lang(request):
#     """Запись языка в сессию"""
#     if request.session.get("lang") is None:
#         request.session["lang"] = Lang.objects.get(is_default=True).slug
#     return {"lang": request.session.get("lang")}
