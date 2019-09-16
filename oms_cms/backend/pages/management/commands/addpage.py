from django.conf import settings
from django.core.management.base import BaseCommand

from oms_cms.backend.pages.models import Pages


class Command(BaseCommand):
    help = 'Add page'

    def handle(self, *args, **options):
        text_home = """The system is open source, written using the Django framework in the Python 
            programming language. This cms allows you to make a website in minutes. You can use the 
            basic template or download from the official site."""
        text_about = """<h1>Install OMS CMS in just 4 steps</h1>
                    <p>pip install oms-cms</p>
                    <p>oms-start</p>
                    <p>cd mysite</p>
                    <p>python manage.py runserver</p>"""
        Pages.objects.create(
            title="Home",
            text=text_home,
            slug="/",
            lang=settings.LANGUAGE_CODE
        )
        Pages.objects.create(
            title="About",
            text=text_about,
            slug='about',
            lang=settings.LANGUAGE_CODE
        )
        self.stdout.write('Success add page')
