from django.conf import settings
from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    help = 'Create project'

    def handle(self, *args, **options):
        call_command('makemigrations', verbosity=3)
        call_command('migrate', verbosity=3)
        # call_command('addlang', settings.LANGUAGE_CODE, verbosity=3)
        self.stdout.write('Success deploy min oms-cms')

