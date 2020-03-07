from rest_framework import generics, permissions
from rest_framework import filters as filters_rf
from django_filters import rest_framework as filters

from oms_cms.backend.menu.models import Menu, MenuItem
from .serializers import MenuSerializer, MenuRetrieveSerializer, MenuItemSerializer, MenuItemExtendedSerializer, \
MenuItemDeleteUpdateCreateSerializer


class MenuListApi(generics.ListAPIView):
    """Список всех меню"""
    permission_classes = [permissions.AllowAny]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    filter_backends = [filters.DjangoFilterBackend,
                       filters_rf.SearchFilter,
                       filters_rf.OrderingFilter]
    filter_fields = ('id', 'status', 'published')
    search_fields = ('name', 'id')
    ordering = ['id']


class MenuRetrieveApi(generics.RetrieveAPIView):
    """Отдельное меню"""
    permission_classes = [permissions.AllowAny]
    queryset = Menu.objects.all()
    serializer_class = MenuRetrieveSerializer
    lookup_field = 'id'


class MenuDeleteUpdateApi(generics.RetrieveUpdateDestroyAPIView):
    """Изменение и удаление меню"""
    permission_classes = [permissions.DjangoModelPermissions]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    lookup_field = 'id'


class MenuCreateApi(generics.CreateAPIView):
    """Создание меню"""
    permission_classes = [permissions.DjangoModelPermissions]
    queryset = Menu.objects.none()
    serializer_class = MenuSerializer


class MenuItemListApi(generics.ListAPIView):
    """Список элементов меню"""
    permission_classes = [permissions.AllowAny]
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    filter_backends = [filters.DjangoFilterBackend,
                       filters_rf.SearchFilter,
                       filters_rf.OrderingFilter]
    filter_fields = ('id', 'parent', 'menu', 'status', 'content_type', 'published')
    search_fields = ('name', 'id', 'title', 'anchor')
    ordering = ['id']


class MenuItemRetrieveApi(generics.RetrieveAPIView):
    """Элемент меню"""
    permission_classes = [permissions.AllowAny]
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemExtendedSerializer
    lookup_field = 'id'


class MenuItemDeleteUpdateApi(generics.RetrieveUpdateDestroyAPIView):
    """Изменение и удаление элементов меню"""
    permission_classes = [permissions.DjangoModelPermissions]
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemDeleteUpdateCreateSerializer
    lookup_field = 'id'


class MenuItemCreateApi(generics.CreateAPIView):
    """Создание элемента меню"""
    permission_classes = [permissions.DjangoModelPermissions]
    queryset = MenuItem.objects.none()
    serializer_class = MenuItemDeleteUpdateCreateSerializer



