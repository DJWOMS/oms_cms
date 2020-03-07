from rest_framework import generics, permissions
from rest_framework import filters as filters_rf
from django_filters import rest_framework as filters

from oms_cms.backend.pages.models import Pages, BlockPage
from .serializers import PagesListSerializer, PagesSerializerRetrieve, BlockPageSerializer, BlockPageCreateSerializer


class PagesListApi(generics.ListAPIView):
    """Список всех страниц"""
    permission_classes = [permissions.AllowAny]
    queryset = Pages.objects.all()
    serializer_class = PagesListSerializer
    filter_backends = [filters.DjangoFilterBackend,
                       filters_rf.SearchFilter,
                       filters_rf.OrderingFilter]
    filter_fields = ('id', 'published')
    search_fields = ['id', 'title', 'slug']
    ordering = ['id']


class PagesRetrieveWithId(generics.RetrieveAPIView):
    """Просмотр информации об отдельной странице (доступ по ID)"""
    permission_classes = [permissions.AllowAny]
    queryset = Pages.objects.all()
    lookup_field = 'id'
    serializer_class = PagesSerializerRetrieve


class PagesDeleteUpdateWithId(generics.RetrieveUpdateDestroyAPIView):
    """Удаление и изменение страницы (доступ по ID)"""
    permission_classes = [permissions.DjangoModelPermissions]
    queryset = Pages.objects.all()
    lookup_field = 'id'
    serializer_class = PagesSerializerRetrieve


class PagesCreate(generics.CreateAPIView):
    """Создание страницы"""
    permission_classes = [permissions.DjangoModelPermissions]
    serializer_class = PagesSerializerRetrieve
    queryset = Pages.objects.none()  # Required for DjangoModelPermissions


class BlockPageListApi(generics.ListAPIView):
    """Список всех блоков информации для старницы"""
    permission_classes = [permissions.AllowAny]
    queryset = BlockPage.objects.all()
    serializer_class = BlockPageSerializer
    filter_backends = [filters.DjangoFilterBackend,
                       filters_rf.SearchFilter,
                       filters_rf.OrderingFilter]
    filter_fields = ('id', 'page_id')
    search_fields = ['id', 'title']
    ordering = ['id']


class BlockPageDeleteUpdateWithId(generics.RetrieveUpdateDestroyAPIView):
    """Удаление и изменение блока информации для старницы (доступ по ID)"""
    permission_classes = [permissions.DjangoModelPermissions]
    queryset = BlockPage.objects.all()
    lookup_field = 'id'
    serializer_class = BlockPageSerializer


class BlockPageRetrieveWithId(generics.RetrieveAPIView):
    """Просмотр блока информации для старницы (доступ по ID)"""
    permission_classes = [permissions.AllowAny]
    queryset = BlockPage.objects.all()
    lookup_field = 'id'
    serializer_class = BlockPageSerializer


class BlockPageCreate(generics.CreateAPIView):
    """Создание блока информации для старницы"""
    permission_classes = [permissions.DjangoModelPermissions]
    serializer_class = BlockPageCreateSerializer
    queryset = BlockPage.objects.none()  # Required for DjangoModelPermissions