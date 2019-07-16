from django import template
from django.contrib.contenttypes.models import ContentType
from django.utils.safestring import mark_safe

from oms_cms.backend.oms_seo.models import Seo

register = template.Library()


@register.inclusion_tag('base/tags/oms_seo/seo-tag.html', takes_context=True)
def seo(context, related_object):
    related_object_type = ContentType.objects.get_for_model(related_object)
    r_object = Seo.objects.filter(
        content_type__pk=related_object_type.id,
        object_id=related_object.id,
    ).first()
    r =''# mark_safe("{% block title %}{0}{% endblock description %}".format(r_object.title_page, r_object.description_page))
    print(r)
    return {"object": r_object}
