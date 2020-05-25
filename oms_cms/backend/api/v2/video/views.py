from rest_framework import generics, permissions
from rest_framework import filters as filters_rf

from oms_cms.backend.video.models import Video
from .serializers import VideoSerializer


class VideoListApi(generics.ListAPIView):
    """Список всех видео"""
    permission_classes = [permissions.AllowAny]
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    filter_backends = [filters_rf.SearchFilter,
                       filters_rf.OrderingFilter]
    search_fields = ['title', 'slug']
    ordering = ['id']


class VideoRetrieveApi(generics.RetrieveAPIView):
    """Просмотр отдельного видео"""
    permission_classes = [permissions.AllowAny]
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    lookup_field = 'id'


class VideoUpdateDeleteApi(generics.RetrieveUpdateDestroyAPIView):
    """Изменение и удаление видео"""
    permission_classes = [permissions.DjangoModelPermissions]
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    lookup_field = 'id'


class VideoCreateApi(generics.CreateAPIView):
    """Создание видео"""
    permission_classes = [permissions.DjangoModelPermissions]
    queryset = Video.objects.none()
    serializer_class = VideoSerializer