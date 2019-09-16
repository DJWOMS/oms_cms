from django import template
from django.contrib.contenttypes.models import ContentType
from django.utils.safestring import mark_safe

from oms_cms.backend.oms_seo.models import Seo, ConnectSSModel, CounterForSite

register = template.Library()


@register.inclusion_tag('base/tags/oms_seo/seo-tag.html')
def seo(related_object):
    """Вывод СЕО данных description & title"""
    related_object_type = ContentType.objects.get_for_model(related_object)
    r_object = Seo.objects.filter(
        content_type__pk=related_object_type.id,
        object_id=related_object.id,
    ).first()
    return {"object": r_object}


@register.simple_tag
def search_system(name):
    """Подключение поисковых систем"""
    system = ConnectSSModel.objects.filter(name=name)
    if system.exists():
        return system.first().key
    else:
        return ''


@register.simple_tag
def counter_system(name):
    """Вывод кода счетчика по имени"""
    system = CounterForSite.objects.filter(name=name, published=True)
    if system.exists():
        return mark_safe(system.first().code)
    else:
        return ''


@register.simple_tag
def counter_system_all():
    """Вывод всех счетчиков"""
    system = CounterForSite.objects.filter(published=True)
    if system.exists():
        return mark_safe(''.join(s.code for s in system))
    else:
        return ''
