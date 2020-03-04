from rest_framework import generics, permissions
from rest_framework import filters as filters_rf
from django_filters import rest_framework as filters

from oms_cms.backend.video.models import Video
from .serializers import VideoSerializer


class VideoListApi(generics.ListAPIView):
    """Список всех видео"""
    permission_classes = [permissions.AllowAny]
    queryset = Video.objects.all()
    serializer_class = VideoSerializer



    ######## Ошибка при попытке добавить видео ############################