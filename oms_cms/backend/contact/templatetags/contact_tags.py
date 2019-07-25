from django import template
from django.template.loader import get_template

from oms_cms.backend.contact.models import Contact, Feedback
from oms_cms.backend.contact.forms import FeedbackFullForm
from django.forms.models import modelform_factory

register = template.Library()


@register.inclusion_tag('base/tags/base_tag.html', takes_context=True)
def contact(context, name=None, template='base/tags/contact/contact_block_tag.html'):
    """Вывод контактов по имени"""
    if name is not None:
        try:
            context = Contact.objects.get(name__icontains=name, lang__slug=context["request"].session.get("lang"))
        except Contact.DoesNotExist:
            return {'template': template}
    else:
        context = Contact.objects.filter(lang__slug=context["request"].session.get("lang")).first()
        # context = Contact.objects.filter().first()
    return {'template': template, "contact": context}


@register.simple_tag()
def gen_form(*args):
    if args:
        form = modelform_factory(Feedback, fields=(args))
    else:
        form = modelform_factory(Feedback, fields=('__all__'))
    # form.prefix = "aform_pre"
    return form


