from django.core.management.base import BaseCommand
from oms_cms.backend.languages.models import Lang


class Command(BaseCommand):
    help = 'Add lang'

    def handle(self, *args, **options):
        Lang.objects.create(name="Русский", slug="ru", is_default=True)
        Lang.objects.create(name="English", slug="en")
        # LangDefault.objects.create(lang_default=lang)
        self.stdout.write('Success add lang')


