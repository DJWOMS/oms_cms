from django.core.management.base import BaseCommand
from oms_cms.backend.social_networks.models import SocialNetworks


class Command(BaseCommand):
    help = 'Add soc. networks'

    def handle(self, *args, **options):
        SocialNetworks.objects.create(
            title="Facebook",
            icon_ui='facebook',
            link="https://facebook.com")
        SocialNetworks.objects.create(
            title="Instagram",
            icon_ui='instagram',
            link="https://instagram.com")
        SocialNetworks.objects.create(
            title="Twitter",
            icon_ui='twitter',
            link="https://twitter.com")
        SocialNetworks.objects.create(
            title="VK",
            icon_ui='vk',
            link="https://vk.com")
        self.stdout.write('Success soc. networks')
