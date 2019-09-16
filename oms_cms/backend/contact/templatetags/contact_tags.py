from django import template

from oms_cms.backend.contact.models import Contact, Feedback
from django.forms.models import modelform_factory

register = template.Library()


def search_contact(context, name=None):
    """Queryset контактов по имени и языку"""
    if name is not None:
        try:
            contacts = Contact.objects.get(name__icontains=name, lang=context["request"].LANGUAGE_CODE)
        except Contact.DoesNotExist:
            return None
    else:
        contacts = Contact.objects.filter(lang=context["request"].LANGUAGE_CODE).first()
    return contacts


@register.inclusion_tag('base/tags/base_tag.html', takes_context=True)
def contact(context, name=None, template='base/tags/contact/contact_block_tag.html'):
    """Вывод контактов по имени"""
    return {'template': template, "contact": search_contact(context, name)}


@register.simple_tag(takes_context=True)
def for_contact(context, name=None):
    """Вывод контактов по имени без шаблона"""
    return search_contact(context, name)


@register.simple_tag()
def gen_form(*args):
    """Генерация формы для обратной связи"""
    if args:
        form = modelform_factory(Feedback, fields=(args))
    else:
        form = modelform_factory(Feedback, fields=('__all__'))
    return form


