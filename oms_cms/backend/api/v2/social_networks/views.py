from rest_framework import generics, permissions
from rest_framework import filters as filters_rf

from oms_cms.backend.social_networks.models import SocialNetworks
from .serializers import SocialNetworksSerializer


class SocialNetworksListApi(generics.ListAPIView):
    """Список всех партнеров"""
    permission_classes = [permissions.AllowAny]
    queryset = SocialNetworks.objects.all()
    serializer_class = SocialNetworksSerializer
    filter_backends = [filters_rf.SearchFilter,
                       filters_rf.OrderingFilter]
    search_fields = ['title', 'link', 'id']
    ordering = ['id']


class SocialNetworksDeleteUpdateRetrieveWithId(generics.RetrieveUpdateDestroyAPIView):
    """Удаление, изменение и просмотр социальных сетей (доступ по ID)"""
    permission_classes = [permissions.DjangoModelPermissions]
    queryset = SocialNetworks.objects.all()
    lookup_field = 'id'
    serializer_class = SocialNetworksSerializer


class SocialNetworksCreate(generics.CreateAPIView):
    """Добавление социальных сетей"""
    permission_classes = [permissions.DjangoModelPermissions]
    serializer_class = SocialNetworksSerializer
    queryset = SocialNetworks.objects.none()  # Required for DjangoModelPermissions



