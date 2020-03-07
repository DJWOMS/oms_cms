from rest_framework import generics, permissions
from rest_framework import filters as filters_rf
from django_filters import rest_framework as filters

from oms_cms.backend.comments.models import OmsComment
from .serializers import OmsCommentSerializer, OmsCommentDeleteUpdateCreateSerializer


class OmsCommentListApi(generics.ListAPIView):
    """Список всех комментариев"""
    permission_classes = [permissions.AllowAny]
    queryset = OmsComment.objects.all()
    serializer_class = OmsCommentSerializer
    filter_backends = [filters.DjangoFilterBackend,
                       filters_rf.SearchFilter,
                       filters_rf.OrderingFilter]
    filter_fields = ('id', 'user', 'is_public', 'is_removed', 'published', 'tree_id',
                     'level', 'site', 'parent', 'children')
    search_fields = ['user_name', 'user_email', 'comment']
    ordering = ['id']


class OmsCommentApi(generics.RetrieveAPIView):
    """Просмотр комментария (доступ по ID)"""
    permission_classes = [permissions.AllowAny]
    queryset = OmsComment.objects.all()
    lookup_field = 'id'
    serializer_class = OmsCommentSerializer


class OmsCommentDeleteUpdateWithId(generics.RetrieveUpdateDestroyAPIView):
    """Удаление и изменение комментария (доступ по ID)"""
    permission_classes = [permissions.DjangoModelPermissions]
    queryset = OmsComment.objects.all()
    lookup_field = 'id'
    serializer_class = OmsCommentDeleteUpdateCreateSerializer


class OmsCommentCreate(generics.CreateAPIView):
    """Создание комментария"""
    permission_classes = [permissions.DjangoModelPermissions]
    serializer_class = OmsCommentDeleteUpdateCreateSerializer
    queryset = OmsComment.objects.none()  # Required for DjangoModelPermissions




