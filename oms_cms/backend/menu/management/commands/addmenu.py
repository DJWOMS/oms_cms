from django.core.management.base import BaseCommand
from oms_cms.backend.menu.models import Menu, MenuItem


class Command(BaseCommand):
    help = 'Add menu'

    def handle(self, *args, **options):
        menu = Menu.objects.create(name="Верхнее")
        MenuItem.objects.create(title="Главная", name="home", menu=menu)
        MenuItem.objects.create(title="Новости", name="news", menu=menu)

        menu = Menu.objects.create(name="Верхнее 2")
        MenuItem.objects.create(title="Контакты", name="contact", menu=menu)

        self.stdout.write('Success menu')


