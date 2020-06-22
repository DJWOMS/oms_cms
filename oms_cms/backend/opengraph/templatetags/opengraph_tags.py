from django import template
from django.contrib.contenttypes.models import ContentType

from oms_cms.backend.opengraph.models import OpenGraph

register = template.Library()


@register.inclusion_tag('base/tags/opengraph/opengraph-tag.html')
def open_graph(related_object):
    """Вывод opengraph данных """
    related_object_type = ContentType.objects.get_for_model(related_object)
    r_object = OpenGraph.objects.filter(
        content_type__pk=related_object_type.id,
        object_id=related_object.id,
    ).first()
    return {"object": r_object, "r_object": related_object}

