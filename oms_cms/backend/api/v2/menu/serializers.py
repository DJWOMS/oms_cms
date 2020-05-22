from rest_framework import serializers
from oms_cms.backend.menu.models import Menu, MenuItem
from django.contrib.contenttypes.models import ContentType


class ContentTypeSerializer(serializers.ModelSerializer):
    """Сериализация content_type"""
    class Meta:
        model = ContentType
        fields = ('id', 'app_label', 'model', 'objects')


class MenuItemChildSerializer(serializers.ModelSerializer):
    """Сериализация дочернего элемента меню"""
    class Meta:
        model = MenuItem
        fields = ('id', 'menu', 'title', 'name')


class MenuItemInMenuListSerializer(serializers.ModelSerializer):
    """Сериализация элементов меню в списке меню"""
    children = MenuItemChildSerializer(many=True, read_only=True)
    parent = MenuItemChildSerializer(read_only=True)
    content_type = ContentTypeSerializer(read_only=True)
    class Meta:
        model = MenuItem
        fields = ('id', 'title', 'name', 'icon', 'status', 'url', 'anchor', 'content_type',
                  'object_id', 'sort', 'published', 'parent', 'children')


class MenuListSerializer(serializers.ModelSerializer):
    """Сериализация всех меню"""
    menu_items = MenuItemInMenuListSerializer(many=True)
    class Meta:
        model = Menu
        fields = ('id', 'name', 'status', 'published', 'menu_items')


class MenuItemInMenuRetrieveSerializer(serializers.ModelSerializer):
    """Сериализация элементов меню в отдельном меню"""
    children = MenuItemInMenuListSerializer(many=True, read_only=True)
    parent = MenuItemChildSerializer(read_only=True)
    content_type = ContentTypeSerializer(read_only=True)
    class Meta:
        model = MenuItem
        fields = ('id', 'title', 'name', 'icon', 'status', 'url', 'anchor', 'content_type',
                  'object_id', 'sort', 'published', 'parent', 'children')


class MenuRetrieveSerializer(serializers.ModelSerializer):
    """Сериализация меню"""
    menu_items = MenuItemInMenuRetrieveSerializer(many=True)
    class Meta:
        model = Menu
        fields = ('id', 'name', 'status', 'published', 'menu_items')


class MenuDeleteUpdateCreateSerializer(serializers.ModelSerializer):
    """Сериализация меню"""
    class Meta:
        model = Menu
        fields = '__all__'


class MenuItemSerializer(serializers.ModelSerializer):
    """Сериализация пункта меню"""
    class Meta:
        model = MenuItem
        fields = '__all__'
