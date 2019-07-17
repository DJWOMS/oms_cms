from django import template
from django.contrib.contenttypes.models import ContentType

from oms_cms.backend.oms_seo.models import Seo

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
