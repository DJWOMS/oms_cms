from rest_framework import serializers

from oms_cms.backend.video.models import Video


class VideoSerializer(serializers.ModelSerializer):
    """сериализация видео"""
    class Meta:
        model = Video
        fields = '__all__'


