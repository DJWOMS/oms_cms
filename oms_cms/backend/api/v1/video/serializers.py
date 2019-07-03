from rest_framework import serializers

from oms_cms.backend.api.v1.photologue.serializers import ImageSerializerField
from oms_cms.backend.video.models import Video


class VideoSerializer(serializers.ModelSerializer):
    """Video"""
    preview = serializers.URLField(read_only=True, source='preview.url')
    image_alt = ImageSerializerField(read_only=True, source='preview.url')

    class Meta:
        model = Video
        fields = ("title", "slug", "video_id", "preview", "image_alt", "duration", "url")
