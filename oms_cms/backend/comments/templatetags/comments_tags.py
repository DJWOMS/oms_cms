from django import template

register = template.Library()


@register.inclusion_tag('base/tags/base_tag.html', takes_context=True)
def comments_show(context, model, template='base/tags/comments/comments.html'):
    """Вывод комментариев в шаблон"""
    return {"template": template, "comments": model.comments.filter(published=True), "context": context}


@register.simple_tag
def for_comments(model):
    """Вывод комментариев"""
    return model.comments.filter(published=True)
