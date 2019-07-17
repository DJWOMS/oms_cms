import subprocess

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Create start project'

    def add_arguments(self, parser):
        parser.add_argument("name", type=str)

    def handle(self, *args, **options):
        if options["site"]:
            subprocess.call(
                "django-admin startproject {} --template=https://github.com/DJWOMS/oms_project/archive/master.zip".format(
                    options["site"]),
                    shell=True
            )
        self.stdout.write('Success start project')
