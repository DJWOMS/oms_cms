from django.core.management.base import BaseCommand
from oms_cms.backend.languages.models import LangDefault, Lang


class Command(BaseCommand):
    help = 'Add lang'

    def handle(self, *args, **options):
        lang = Lang.objects.create(name="Русский", slug="ru")
        Lang.objects.create(name="English", slug="en")
        LangDefault.objects.create(lang_default=lang)
        self.stdout.write('Success add lang')


