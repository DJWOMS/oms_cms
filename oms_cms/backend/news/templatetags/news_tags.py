from django import template
from django.template.loader import get_template

from oms_cms.backend.news.models import Post

register = template.Library()


@register.inclusion_tag('base/tags/news/news_base_tag.html')
def list_post(category=None, template='base/tags/news/news_block_tag.html'):
    if category is not None:
        context = Post.objects.filter(category__name__icontains=category)
    else:
        context = Post.objects.all()
    return {'template': template, "post_list": context}


# register.inclusion_tag(template_html)(contact)


