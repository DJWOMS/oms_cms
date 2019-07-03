from django.core.management.base import BaseCommand
from oms_cms.backend.menu.models import Menu, MenuItem, ItemMenuLang


class Command(BaseCommand):
    help = 'Add menu'

    def handle(self, *args, **options):
        menu = Menu.objects.create(name="Верхнее", slug="head")
        item = MenuItem.objects.create(name="home", menu=menu)
        ItemMenuLang.objects.create(title="Главная", item=item, lang_id=1)
        item = MenuItem.objects.create(name="shop", menu=menu)
        ItemMenuLang.objects.create(title="Магазины", item=item, lang_id=1)
        item = MenuItem.objects.create(name="service", menu=menu)
        ItemMenuLang.objects.create(title="Услуги и развлечения", item=item, lang_id=1)
        item = MenuItem.objects.create(name="food", menu=menu)
        ItemMenuLang.objects.create(title="Еда", item=item, lang_id=1)
        item = MenuItem.objects.create(name="news", menu=menu)
        ItemMenuLang.objects.create(title="Новости", item=item, lang_id=1)

        menu = Menu.objects.create(name="Верхнее 2", slug="head-2")
        item = MenuItem.objects.create(name="contact", menu=menu)
        ItemMenuLang.objects.create(title="Контакты", item=item, lang_id=1)
        item = MenuItem.objects.create(name="about", menu=menu)
        ItemMenuLang.objects.create(title="О ТРЦ", item=item, lang_id=1)
        item = MenuItem.objects.create(name="arenda", menu=menu)
        ItemMenuLang.objects.create(title="Арендаторам", item=item, lang_id=1)

        self.stdout.write('Success menu')


