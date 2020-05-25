from rest_framework import serializers
from oms_cms.backend.menu.models import Menu, MenuItem
from django.contrib.contenttypes.models import ContentType


class ContentTypeSerializer(serializers.ModelSerializer):
    """Сериализация content_type"""
    class Meta:
        model = ContentType
        fields = ('id', 'app_label', 'model', 'objects')


class MenuSerializer(serializers.ModelSerializer):
    """Сериализация меню"""
    class Meta:
        model = Menu
        fields = ('id', 'name', 'status', 'published', 'menu_items')


class MenuItemShortSerializer(serializers.ModelSerializer):
    """Сериализация элементов меню"""
    class Meta:
        model = MenuItem
        fields = ('id', 'title', 'content_type', 'children')


class MenuRetrieveSerializer(serializers.ModelSerializer):
    """Сериализация меню"""
    menu_items = MenuItemShortSerializer(many=True)
    class Meta:
        model = Menu
        fields = '__all__'


class MenuItemChildShortSerializer(serializers.ModelSerializer):
    """Сериализация дочернего элемента меню"""
    class Meta:
        model = MenuItem
        fields = ('id',)


class MenuItemSerializer(serializers.ModelSerializer):
    """Сериализация элементов меню"""
    children = MenuItemChildShortSerializer(many=True)
    content_type = ContentTypeSerializer()
    class Meta:
        model = MenuItem
        fields = '__all__'


class MenuItemChildExtendedSerializer(serializers.ModelSerializer):
    """Сериализация дочернего элемента меню"""
    content_type = ContentTypeSerializer()
    children = MenuItemChildShortSerializer(many=True)
    class Meta:
        model = MenuItem
        fields = ('id', 'title', 'name', 'children', 'status', 'content_type', 'object_id', 'published')


class MenuItemExtendedSerializer(serializers.ModelSerializer):
    """Сериализация элементов меню"""
    content_type = ContentTypeSerializer()
    children = MenuItemChildExtendedSerializer(many=True)
    class Meta:
        model = MenuItem
        fields = '__all__'


class MenuItemDeleteUpdateCreateSerializer(serializers.ModelSerializer):
    """Сериализация элементов меню"""
    class Meta:
        model = MenuItem
        fields = '__all__'

