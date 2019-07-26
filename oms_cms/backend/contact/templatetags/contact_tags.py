from django import template

from oms_cms.backend.contact.models import Contact, Feedback
from django.forms.models import modelform_factory

register = template.Library()


def search_contact(context, name=None):
    """Queryset контактов по имени и языку"""
    if name is not None:
        try:
            context = Contact.objects.get(name__icontains=name, lang__slug=context["request"].session.get("lang"))
        except Contact.DoesNotExist:
            return {'template': template}
    else:
        context = Contact.objects.filter(lang__slug=context["request"].session.get("lang")).first()
    return context


@register.inclusion_tag('base/tags/base_tag.html', takes_context=True)
def contact(context, name=None, template='base/tags/contact/contact_block_tag.html'):
    """Вывод контактов по имени"""
    context = search_contact(context, name)
    return {'template': template, "contact": context}


@register.simple_tag(takes_context=True)
def for_contact(context, name=None):
    """Вывод контактов по имени без шаблона"""
    context = search_contact(context, name)
    return context


@register.simple_tag()
def gen_form(*args):
    """Генерация формы для обратной связи"""
    if args:
        form = modelform_factory(Feedback, fields=(args))
    else:
        form = modelform_factory(Feedback, fields=('__all__'))
    return form


