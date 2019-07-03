from rest_framework import generics, permissions

from oms_cms.backend.video.models import Video
from .serializers import VideoSerializer


class VideoList(generics.ListAPIView):
    """Список всех видео"""
    permission_classes = [permissions.AllowAny]
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


class OneVideo(generics.RetrieveAPIView):
    """Вывод одного видео по slug"""
    permission_classes = [permissions.AllowAny]
    serializer_class = VideoSerializer
    queryset = Video.objects.all()
    lookup_field = "slug"


class InstVideo(generics.ListAPIView):
    """Вывод видео instagram"""
    permission_classes = [permissions.AllowAny]
    serializer_class = VideoSerializer

    def get_queryset(self):
        return Video.objects.filter(ints_video=True)


class BanquetVideo(generics.ListAPIView):
    """Вывод видео banquet"""
    permission_classes = [permissions.AllowAny]
    serializer_class = VideoSerializer

    def get_queryset(self):
        return Video.objects.filter(banquet_video=True)


