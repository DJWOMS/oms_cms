from rest_framework import serializers

from oms_cms.backend.info_block.models import InfoBlock, BlockField
from oms_cms.backend.api.v1.photologue.serializers import PhotoSerializer, GallerySerializer


class BlockFieldSerializer(serializers.ModelSerializer):
    """Поля инфо блоков"""
    photo = PhotoSerializer()

    class Meta:
        model = BlockField
        fields = ("sub_title",
                  "desc",
                  "photo"
                  )


class InfoBlockSerializer(serializers.ModelSerializer):
    """Информационные блоки"""
    slider = GallerySerializer()
    options = BlockFieldSerializer(many=True)

    class Meta:
        model = InfoBlock
        fields = ("title",
                  "sub_title",
                  "desc",
                  "slider",
                  "section",
                  "options"
                  )
