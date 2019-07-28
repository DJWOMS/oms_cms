from django.core.management.base import BaseCommand

from oms_cms.backend.languages.models import Lang
from oms_cms.backend.contact.models import Contact, ContactFields, ContactSocNet


class Command(BaseCommand):
    help = 'Add contact'

    def handle(self, *args, **options):
        contact = Contact.objects.create(name="Header", slug="contact", lang=Lang.objects.get(is_default=True))
        ContactFields.objects.create(
            text="Адрес клуба",
            text_two="Лобачевского 74",
            icon_ui="location",
            contact=contact
        )
        ContactFields.objects.create(
            text="06:00 01:00",
            text_two="Сейчас открыт",
            icon_ui="clock",
            contact=contact
        )
        ContactFields.objects.create(
            text="8 495 220-26-33",
            text_two="Общий телефон",
            icon_ui="phone",
            contact=contact
        )
        ContactSocNet.objects.create(
            contact_soc=contact,
            your_id="djwoms",
            link_id=1
        )
        ContactSocNet.objects.create(
            contact_soc=contact,
            your_id="djwoms",
            link_id=2
        )

        contact_footer = Contact.objects.create(
            name="Footer",
            slug="contact-footer",
            lang=Lang.objects.get(is_default=True)
        )
        ContactFields.objects.create(
            text="Адрес клуба",
            text_two="Лобачевского 74",
            icon_ui="home",
            contact=contact_footer
        )
        ContactFields.objects.create(
            text="Парковка",
            text_two="24/7",
            icon_ui="commenting",
            contact=contact_footer
        )
        self.stdout.write('Success add contact')


