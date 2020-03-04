from rest_framework import serializers

from oms_cms.backend.info_block.models import InfoBlock
from oms_cms.backend.api.v2.pages.serializers import GalleryBlockPageSerializer


class InfoBlockSerializer(serializers.ModelSerializer):
    """Сериализация InfoBlock"""
    class Meta:
        model = InfoBlock
        fields = '__all__'


class InfoBlockRetrieveSerializer(serializers.ModelSerializer):
    """Сериализация InfoBlock"""
    slider = GalleryBlockPageSerializer()
    class Meta:
        model = InfoBlock
        fields = ('id', 'lang', 'slug', 'title', 'sub_title', 'description', 'slider')


