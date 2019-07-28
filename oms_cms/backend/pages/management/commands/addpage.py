from django.core.management.base import BaseCommand

from oms_cms.backend.languages.models import Lang
from oms_cms.backend.pages.models import Pages


class Command(BaseCommand):
    help = 'Add page'

    def handle(self, *args, **options):
        Pages.objects.create(
            title="Главная",
            text='Page test',
            slug=None,
            lang=Lang.objects.get(is_default=True)
        )
        Pages.objects.create(
            title="О нас",
            text='Page about',
            slug='about',
            lang=Lang.objects.get(is_default=True)
        )
        self.stdout.write('Success page')
