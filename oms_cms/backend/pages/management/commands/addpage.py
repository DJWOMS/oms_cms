from django.core.management.base import BaseCommand
from oms_cms.backend.pages.models import Pages


class Command(BaseCommand):
    help = 'Add page'

    def handle(self, *args, **options):
        Pages.objects.create(
            title="Главная",
            text='Page test',
            slug='',
            lang_id=1
        )
        Pages.objects.create(
            title="О нас",
            text='Page about',
            slug='about',
            lang_id=1
        )
        self.stdout.write('Success page')
