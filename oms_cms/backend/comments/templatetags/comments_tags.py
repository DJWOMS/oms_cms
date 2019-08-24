from django import template
from django.contrib.contenttypes.models import ContentType
from django.forms import modelform_factory

from oms_cms.backend.comments.models import OmsComment

register = template.Library()


@register.inclusion_tag('base/tags/base_tag.html', takes_context=True)
def comments_show(context, model, template='base/tags/comments/comments.html'):
    """Вывод комментариев в шаблон"""
    return {"template": template, "comments": model.comments.filter(published=True), "context": context}


@register.simple_tag
def for_comments(model):
    """Вывод комментариев"""
    return model.comments.filter(published=True)


@register.simple_tag()
def comment_form(*args):
    """Генерация формы для комментариев"""
    if args:
        form = modelform_factory(OmsComment, fields=(args))
    else:
        form = modelform_factory(OmsComment, fields=('__all__'))
    return form


@register.simple_tag()
def comment_url(app_model, pk):
    return f"/?model={app_model}&pk={pk}"
