from django.core.management.base import BaseCommand

from oms_cms.backend.languages.models import Lang
from oms_cms.backend.menu.models import Menu, MenuItem


class Command(BaseCommand):
    help = 'Add menu'

    def handle(self, *args, **options):
        menu = Menu.objects.create(name="Main")
        MenuItem.objects.create(
            title="Главная",
            name="home",
            menu=menu,
            lang=Lang.objects.get(is_default=True)
        )
        MenuItem.objects.create(
            title="Новости",
            name="news",
            menu=menu,
            lang=Lang.objects.get(is_default=True)
        )

        menu = Menu.objects.create(name="Footer")
        MenuItem.objects.create(title="Контакты", name="contact", menu=menu, lang=Lang.objects.get(is_default=True))

        self.stdout.write('Success menu')


