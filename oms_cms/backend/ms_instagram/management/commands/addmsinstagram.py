from django.core.management.base import BaseCommand
from oms_cms.backend.ms_instagram.models import ConfigMSInstagram


class Command(BaseCommand):
    help = 'Add soc. networks'

    def handle(self, *args, **options):
        ConfigMSInstagram.objects.create(
            name="Instagram",
            client_id='bb9b7da5aa4d4c47a414d0be1031ba97',
            client_secret="4d3995425c0f4ffa9bd2f93bb9c1bfec",
            redirect_uri="http://139.59.223.194/insta/oauth_callback/",
            access_token=""
        )
        self.stdout.write('Success ms_instagram')
