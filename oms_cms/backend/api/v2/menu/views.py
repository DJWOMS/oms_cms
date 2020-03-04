from rest_framework import generics, permissions
from rest_framework import filters as filters_rf
from django_filters import rest_framework as filters

from oms_cms.backend.menu.models import Menu, MenuItem
from .serializers import MenuItemSerializer, MenuListSerializer, MenuRetrieveSerializer, MenuDeleteUpdateCreateSerializer, MenuItemInMenuRetrieveSerializer


class MenuListApi(generics.ListAPIView):
    """Список всех меню"""
    permission_classes = [permissions.AllowAny]
    queryset = Menu.objects.all()
    serializer_class = MenuListSerializer
    filter_backends = [filters.DjangoFilterBackend,
                       filters_rf.SearchFilter,
                       filters_rf.OrderingFilter]
    filter_fields = ('id', 'status', 'published')
    search_fields = ['name']
    ordering = ['id']


class MenuRetrieveWithId(generics.RetrieveAPIView):
    """Просмотр информации об отдельном меню (доступ по ID)"""
    permission_classes = [permissions.AllowAny]
    queryset = Menu.objects.all()
    lookup_field = 'id'
    serializer_class = MenuRetrieveSerializer


class MenuDeleteUpdateWithId(generics.RetrieveUpdateDestroyAPIView):
    """Удаление и изменение меню (доступ по ID)"""
    permission_classes = [permissions.DjangoModelPermissions]
    queryset = Menu.objects.all()
    lookup_field = 'id'
    serializer_class = MenuDeleteUpdateCreateSerializer


class MenuCreate(generics.CreateAPIView):
    """Создание меню"""
    permission_classes = [permissions.DjangoModelPermissions]
    serializer_class = MenuDeleteUpdateCreateSerializer
    queryset = Menu.objects.none()  # Required for DjangoModelPermissions


class MenuItemListApi(generics.ListAPIView):
    """Список всех элементов меню"""
    permission_classes = [permissions.AllowAny]
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemInMenuRetrieveSerializer
    filter_backends = [filters.DjangoFilterBackend,
                       filters_rf.SearchFilter,
                       filters_rf.OrderingFilter]
    filter_fields = ('id', 'status', 'published', 'parent')
    search_fields = ['title', 'name']
    ordering = ['id']


class MenuItemRetrieveWithId(generics.RetrieveAPIView):
    """Просмотр информации об отдельном элементе меню (доступ по ID)"""
    permission_classes = [permissions.AllowAny]
    queryset = MenuItem.objects.all()
    lookup_field = 'id'
    serializer_class = MenuItemInMenuRetrieveSerializer


class MenuItemDeleteUpdateWithId(generics.RetrieveUpdateDestroyAPIView):
    """Удаление и изменение элемента меню (доступ по ID)"""
    permission_classes = [permissions.DjangoModelPermissions]
    queryset = MenuItem.objects.all()
    lookup_field = 'id'
    serializer_class = MenuItemSerializer



class MenuItemCreate(generics.CreateAPIView):
    """Создание элемента меню"""
    permission_classes = [permissions.DjangoModelPermissions]
    serializer_class = MenuItemSerializer
    queryset = MenuItem.objects.none()  # Required for DjangoModelPermissions