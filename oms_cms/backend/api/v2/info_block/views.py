from rest_framework import generics, permissions
from rest_framework import filters as filters_rf
from django_filters import rest_framework as filters

from oms_cms.backend.info_block.models import InfoBlock
from .serializers import InfoBlockSerializer, InfoBlockRetrieveSerializer


class InfoBlockListApi(generics.ListAPIView):
    """Список всех InfoBlock"""
    permission_classes = [permissions.AllowAny]
    queryset = InfoBlock.objects.all()
    serializer_class = InfoBlockSerializer
    filter_backends = [filters.DjangoFilterBackend,
                       filters_rf.SearchFilter,
                       filters_rf.OrderingFilter]
    filter_fields = ('id', 'lang', 'slider')
    search_fields = ['slug', 'title', 'sub_title', 'description']
    ordering = ['id']


class InfoBlockRetrieveApi(generics.RetrieveAPIView):
    """Просмотр InfoBlock (доступ по ID)"""
    permission_classes = [permissions.AllowAny]
    queryset = InfoBlock.objects.all()
    lookup_field = 'id'
    serializer_class = InfoBlockRetrieveSerializer


class InfoBlockDeleteUpdateWithId(generics.RetrieveUpdateDestroyAPIView):
    """Удаление и изменение InfoBlock (доступ по ID)"""
    permission_classes = [permissions.DjangoModelPermissions]
    queryset = InfoBlock.objects.all()
    lookup_field = 'id'
    serializer_class = InfoBlockSerializer


class InfoBlockCreate(generics.CreateAPIView):
    """Создание InfoBlock"""
    permission_classes = [permissions.DjangoModelPermissions]
    serializer_class = InfoBlockSerializer
    queryset = InfoBlock.objects.none()  # Required for DjangoModelPermissions

