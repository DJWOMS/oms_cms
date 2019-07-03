from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View

from .models import MenuItem


class MenuLink(View):
    """Переход по ссылке"""

    def get(self, request, url=None):
        print(url)
        # b = MenuItem.objects.get(link=url)
        content_types = ContentType.objects.filter(menuitem__link=url)
        print(content_types)
        # bookmark = ContentType.objects.get_for_model(b)
        # print(bookmark)
        return HttpResponse("fff")
