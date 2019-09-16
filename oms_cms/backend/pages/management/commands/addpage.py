from django.conf import settings
from django.core.management.base import BaseCommand

from oms_cms.backend.pages.models import Pages


class Command(BaseCommand):
    help = 'Add page'

    def handle(self, *args, **options):
        text_home = """<h3>Language</h3>
                 <p>OMS is written in Python, the fastest growing programming language.</p>
                 <h3>Sites</h3>
                 <p>OMS sites are immediately operational after installation and easily expandable.</p>
                 <h3>Security</h3>
                 <p>OMS is developed on Django which includes security.</p>"""
        text_about = """<h1>Install OMS CMS in just 4 steps</h1>
                    <p>pip install oms-cms</p>
                    <p>oms-start</p>
                    <p>cd mysite</p>
                    <p>python manage.py runserver</p>"""
        Pages.objects.create(
            title="Home",
            text=text_home,
            slug=None,
            lang=settings.LANGUAGE_CODE
        )
        Pages.objects.create(
            title="About",
            text=text_about,
            slug='about',
            lang=settings.LANGUAGE_CODE
        )
        self.stdout.write('Success add page')
