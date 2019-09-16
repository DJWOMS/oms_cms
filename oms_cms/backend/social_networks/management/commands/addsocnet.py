from django.core.management.base import BaseCommand
from oms_cms.backend.social_networks.models import SocialNetworks


class Command(BaseCommand):
    help = 'Add soc. networks'

    def handle(self, *args, **options):
        SocialNetworks.objects.create(
            title="Facebook",
            icon_ui='fab fa-facebook',
            link="https://facebook.com")
        SocialNetworks.objects.create(
            title="Instagram",
            icon_ui='fab fa-instagram',
            link="https://instagram.com")
        SocialNetworks.objects.create(
            title="Twitter",
            icon_ui='fab fa-twitter',
            link="https://twitter.com")
        SocialNetworks.objects.create(
            title="VK",
            icon_ui='fab fa-vk',
            link="https://vk.com")
        SocialNetworks.objects.create(
            title="Github",
            icon_ui='fab fa-github',
            link="https://github.com")
        self.stdout.write('Success add soc. networks')
