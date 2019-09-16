from django.core.management.base import BaseCommand
from django.conf import settings

from oms_cms.backend.menu.models import Menu, MenuItem


class Command(BaseCommand):
    help = 'Add menu'

    def handle(self, *args, **options):
        menu = Menu.objects.create(name="Main")
        MenuItem.objects.create(
            title="Home",
            name="home",
            menu=menu,
            lang=settings.LANGUAGE_CODE
        )
        MenuItem.objects.create(
            title="News",
            name="news",
            menu=menu,
            lang=settings.LANGUAGE_CODE
        )

        self.stdout.write('Success add menu')


