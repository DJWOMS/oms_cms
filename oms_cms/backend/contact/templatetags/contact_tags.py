from django import template
from django.template.loader import get_template

from oms_cms.backend.contact.models import Contact

register = template.Library()


@register.inclusion_tag('base/tags/contact/contact_base_tag.html', takes_context=True)
def contact(context, name=None, template='base/tags/contact/contact_block_tag.html'):
    """Вывод контактов по имени"""
    if name is not None:
        try:
            context = Contact.objects.get(name__icontains=name)
        except Contact.DoesNotExist:
            return {'template': template}
    else:
        # context = Contact.objects.filter(lang__slug=context["request"].session.get("lang")).first()
        context = Contact.objects.filter().first()
    return {'template': template, "contact": context}


# register.inclusion_tag(template_html)(contact)


