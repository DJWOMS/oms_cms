# from django.utils.deprecation import MiddlewareMixin
#
# from oms_cms.backend.languages.models import Lang
#
#
# class LanguagesMiddleware(MiddlewareMixin):
#     """Мидлвар для проверки языка из url"""
#     def process_request(self, request):
#         lang = request.path.split("/")[1]
#         if Lang.objects.filter(slug=lang).exists():
#             request.session["lang"] = Lang.objects.get(slug=lang).slug
#         else:
#             request.session["lang"] = Lang.objects.get(is_default=True).slug
