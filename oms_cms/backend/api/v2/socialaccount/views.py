from rest_framework import generics, permissions
from rest_framework import filters as filters_rf
from django_filters import rest_framework as filters

from allauth.socialaccount.models import SocialAccount, SocialApp, SocialToken
from .serializers import SocialAppSerializer, SocialAppExtendedSerializer, SocialAccountSerializer, \
    SocialAccountExtendedSerializer, SocialTokenSerializer, SocialTokenExtendedSerializer


class SocialAppListApi(generics.ListAPIView):
    """Список всех SocialApp"""
    permission_classes = [permissions.DjangoModelPermissions]
    queryset = SocialApp.objects.all()
    serializer_class = SocialAppExtendedSerializer
    filter_backends = [filters.DjangoFilterBackend,
                       filters_rf.SearchFilter,
                       filters_rf.OrderingFilter]
    filter_fields = ('id', 'provider', 'sites')
    search_fields = ['name', 'client_id', 'id']
    ordering = ['id']


class SocialAppRetrieveDeleteUpdateApi(generics.RetrieveUpdateDestroyAPIView):
    """Просмотр, изменение и удаления приложения соц. сети"""
    permission_classes = [permissions.DjangoModelPermissions]
    queryset = SocialApp.objects.all()
    lookup_field = 'id'
    serializer_class = SocialAppSerializer


class SocialAppCreateApi(generics.CreateAPIView):
    """Добавление приложения соц. сети"""
    permission_classes = [permissions.DjangoModelPermissions]
    queryset = SocialApp.objects.none()
    serializer_class = SocialAppSerializer


class SocialAccountListApi(generics.ListAPIView):
    """Список всех аккаунтов соц. сетей"""
    permission_classes = [permissions.DjangoModelPermissions]
    queryset = SocialAccount.objects.all()
    serializer_class = SocialAccountExtendedSerializer
    filter_backends = [filters.DjangoFilterBackend,
                       filters_rf.SearchFilter,
                       filters_rf.OrderingFilter]
    filter_fields = ('id', 'user', 'provider')
    search_fields = ['user__username']
    ordering = ['id']


class SocialAccountRetrieveDeleteUpdateApi(generics.RetrieveUpdateDestroyAPIView):
    """Просмотр, изменение и удаления аккаунта в соц. сети"""
    permission_classes = [permissions.DjangoModelPermissions]
    queryset = SocialAccount.objects.all()
    serializer_class = SocialAccountSerializer
    lookup_field = 'id'


class SocialAccountCreateApi(generics.CreateAPIView):
    """Добавление аккаунта соц. сети"""
    permission_classes = [permissions.DjangoModelPermissions]
    queryset = SocialAccount.objects.none()
    serializer_class = SocialAccountSerializer


class SocialTokenListApi(generics.ListAPIView):
    """Список токенов"""
    permission_classes = [permissions.DjangoModelPermissions]
    queryset = SocialToken.objects.all()
    serializer_class = SocialTokenExtendedSerializer
    filter_backends = [filters.DjangoFilterBackend,
                       filters_rf.SearchFilter,
                       filters_rf.OrderingFilter]
    filter_fields = ('id', 'app', 'account')
    search_fields = ['account__user__username', 'token', 'id']
    ordering = ['id']


class SocialTokenRetrieveDeleteUpdateApi(generics.RetrieveUpdateDestroyAPIView):
    """Просмотр, изменение и удаления токенов"""
    permission_classes = [permissions.DjangoModelPermissions]
    queryset = SocialToken.objects.all()
    serializer_class = SocialTokenSerializer
    lookup_field = 'id'


class SocialTokenCreateApi(generics.CreateAPIView):
    """Добавление токена"""
    permission_classes = [permissions.DjangoModelPermissions]
    queryset = SocialToken.objects.none()
    serializer_class = SocialTokenSerializer
