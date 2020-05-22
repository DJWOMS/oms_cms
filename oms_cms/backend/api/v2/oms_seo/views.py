from rest_framework import generics, permissions
from rest_framework import filters as filters_rf
from django_filters import rest_framework as filters

from oms_cms.backend.oms_seo.models import Seo, ConnectSSModel, CounterForSite
from .serializers import SeoSerializer, SeoCreateSerializer, ConnectSSModelSerializer, CounterForSiteSerializer


class SeoListApi(generics.ListAPIView):
    """Список всех Seo модулей"""
    permission_classes = [permissions.DjangoModelPermissions]
    queryset = Seo.objects.all()
    serializer_class = SeoSerializer
    filter_backends = [filters.DjangoFilterBackend,
                       filters_rf.SearchFilter,
                       filters_rf.OrderingFilter]
    filter_fields = ('id', 'object_id', 'content_type')
    search_fields = ['title_page', 'description_page']
    ordering = ['id']


class SeoDeleteUpdateRetrieveWithId(generics.RetrieveUpdateDestroyAPIView):
    """Удаление, изменение и просмотр Seo модулей (доступ по ID)"""
    permission_classes = [permissions.DjangoModelPermissions]
    queryset = Seo.objects.all()
    lookup_field = 'id'
    serializer_class = SeoCreateSerializer


class SeoCreate(generics.CreateAPIView):
    """Добавление Seo модулей"""
    permission_classes = [permissions.DjangoModelPermissions]
    serializer_class = SeoCreateSerializer
    queryset = Seo.objects.none()  # Required for DjangoModelPermissions


class ConnectSSModelListApi(generics.ListAPIView):
    """Список подключенных ПС"""
    permission_classes = [permissions.DjangoModelPermissions]
    queryset = ConnectSSModel.objects.all()
    serializer_class = ConnectSSModelSerializer
    filter_backends = [filters_rf.SearchFilter,
                       filters_rf.OrderingFilter]
    search_fields = ['name', 'id']
    ordering = ['id']


class ConnectSSModelDeleteUpdateRetrieveWithId(generics.RetrieveUpdateDestroyAPIView):
    """Просмотр, изменение, удаление подключенных ПС"""
    permission_classes = [permissions.DjangoModelPermissions]
    queryset = ConnectSSModel.objects.all()
    lookup_field = 'id'
    serializer_class = ConnectSSModelSerializer


class ConnectSSModelCreate(generics.CreateAPIView):
    """Подключение ПС"""
    permission_classes = [permissions.DjangoModelPermissions]
    serializer_class = ConnectSSModelSerializer
    queryset = ConnectSSModel.objects.none()


class CounterForSiteListApi(generics.ListAPIView):
    """Список счетчиков"""
    permission_classes = [permissions.DjangoModelPermissions]
    queryset = CounterForSite.objects.all()
    serializer_class = CounterForSiteSerializer
    filter_backends = [filters.DjangoFilterBackend,
                       filters_rf.SearchFilter,
                       filters_rf.OrderingFilter]
    filter_fields = ('id', 'published')
    search_fields = ['name']
    ordering = ['id']


class CounterForSiteDeleteUpdateRetrieveWithId(generics.RetrieveUpdateDestroyAPIView):
    """Просмотр, изменение, удаление счетчиков"""
    permission_classes = [permissions.DjangoModelPermissions]
    queryset = CounterForSite.objects.all()
    lookup_field = 'id'
    serializer_class = CounterForSiteSerializer


class CounterForSiteCreate(generics.CreateAPIView):
    """Подключение счетчиков"""
    permission_classes = [permissions.DjangoModelPermissions]
    serializer_class = CounterForSiteSerializer
    queryset = CounterForSite.objects.none()