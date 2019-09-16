# from django.core.management.base import BaseCommand
# from oms_cms.backend.languages.models import Lang


# class Command(BaseCommand):
#     help = 'Add lang'
#
#     def add_arguments(self, parser):
#         parser.add_argument("lang", type=str)
#
#     def handle(self, *args, **options):
#         # if options["lang"]:
#         #     for i in options["lang"]:
#         #         Lang.objects.create(name=i.get("name"), slug=i.get("slug"))
#         # else:
#         if options["lang"] == "ru":
#             Lang.objects.create(name="Русский", slug="ru")
#         else:
#             Lang.objects.create(name="English", slug="en")
#         self.stdout.write('Success add lang')


