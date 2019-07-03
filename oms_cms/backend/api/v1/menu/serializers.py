from rest_framework import serializers

from oms_cms.backend.menu.models import Menu, MenuItem


class MenuSerializer(serializers.ModelSerializer):
    """Меню"""
    class Meta:
        model = Menu
        fields = ("name", "status", "slug")


class MenuItemSerializer(serializers.ModelSerializer):
    """Элементы меню"""
    menu = MenuSerializer()

    class Meta:
        model = MenuItem
        fields = ("name",
                  "menu",
                  "status",
                  "url",
                  "anchor",
                  "object_id")
