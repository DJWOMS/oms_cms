from django.conf import settings
from django.core.management.base import BaseCommand

from oms_cms.backend.languages.models import Lang
from oms_cms.backend.pages.models import Pages


class Command(BaseCommand):
    help = 'Add page'

    def handle(self, *args, **options):
        text_home = """<h3>Язык</h3>
                <p>OMS написана на Python, самом быстрорастущем языке программирования.</p>
                <h3>Сайты</h3>
                <p>Сайты на OMS сразу готовы к работе после установки и легко расширяются.</p>
                <h3>Безопасность</h3>
                <p>OMS разработана на Django который включает безопасность.</p>"""
        text_about = """<h1>Установите OMS CMS всего за 4 шага</h1>
                    <p>pip install oms-cms</p>
                    <p>oms-start</p>
                    <p>cd mysite</p>
                    <p>python manage.py runserver</p>"""
        Pages.objects.create(
            title="Главная",
            text=text_home,
            slug=None,
            lang=Lang.objects.get(slug=settings.LANGUAGE_CODE)
        )
        Pages.objects.create(
            title="О нас",
            text=text_about,
            slug='about',
            lang=Lang.objects.get(slug=settings.LANGUAGE_CODE)
        )
        self.stdout.write('Success page')
