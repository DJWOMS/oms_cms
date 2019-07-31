from django.core.management.base import BaseCommand

from oms_cms.backend.social_networks.models import SocialNetworks

from oms_cms.backend.languages.models import Lang
from oms_cms.backend.contact.models import Contact, ContactFields, ContactSocNet


class Command(BaseCommand):
    help = 'Add contact'

    def handle(self, *args, **options):
        contact = Contact.objects.create(name="Header", slug="contact", lang=Lang.objects.get(is_default=True))
        ContactFields.objects.create(
            text="info@oms-cms.site",
            text_two="",
            icon_ui="fa fa-envelope",
            contact=contact
        )
        ContactFields.objects.create(
            text="+1 111 111-11-11",
            text_two="",
            icon_ui="fa fa-phone",
            contact=contact
        )

        contact_footer = Contact.objects.create(
            name="Footer",
            description="OMS CMS django 2",
            slug="contact-footer",
            lang=Lang.objects.get(is_default=True)
        )
        ContactSocNet.objects.create(
            contact_soc=contact_footer,
            your_id="djangochannel",
            link=SocialNetworks.objects.get(title="VK")
        )
        ContactSocNet.objects.create(
            contact_soc=contact_footer,
            your_id="djangochannel",
            link=SocialNetworks.objects.get(title="Facebook")
        )
        ContactSocNet.objects.create(
            contact_soc=contact_footer,
            your_id="DJWOMS",
            link=SocialNetworks.objects.get(title="Github")
        )
        self.stdout.write('Success add contact')


