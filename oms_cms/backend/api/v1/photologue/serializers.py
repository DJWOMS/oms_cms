import base64
import os
from io import BytesIO

from PIL import Image
from rest_framework import serializers

from photologue.models import Photo, Gallery

from oms_cms.config import settings
from django.conf import settings

BASE_DIR = settings.BASE_DIR


class ImageSerializerField(serializers.Field):

    def to_representation(self, value):
        outputPath = self.to_internal_value(value)
        return outputPath

    def to_internal_value(self, value):
        f = value.split("/").pop().split(".").pop(1)
        if f == "jpeg" or f == "jpg" or f == "webp":
            way = "tmp/img{}.j2p".format(value.split("/").pop().split(".").pop(0))
            outputPath = os.path.joGin(settings.MEDIA_ROOT, way)
            # quality = 50
            try:
                Image.open(settings.MEDIA_ROOT + "/" + way)
            except:
                im = Image.open(BASE_DIR + value[value.rfind('/media'):])
                im.save(outputPath, 'JPEG', optimize=True, quality=60)
            path = settings.MEDIA_URL[:settings.MEDIA_URL.find('media')] + outputPath[outputPath.rfind('media'):]
            return path
        else:
            return value


class PhotoSerializer(serializers.ModelSerializer):
    """Photo"""
    # image = serializers.ImageField(max_length=None, use_url=True, allow_null=True, required=False)
    # image = serializers.ImageField('image.url')
    # image = serializers.SerializerMethodField('get_thumbnail_url')
    image = serializers.URLField(read_only=True, source='image.url')
    image_alt = ImageSerializerField(read_only=True, source='image.url')

    # def get_thumbnail_url(self, obj):
    #     return '%s%s' % (settings.MEDIA_URL, obj.get_absolute_url)

    class Meta:
        model = Photo
        fields = ("id", "image", "image_alt")


class GallerySerializer(serializers.ModelSerializer):
    """Photo"""
    photos = PhotoSerializer(many=True, read_only=True)

    class Meta:
        model = Gallery
        fields = ("id", "title", "description", "photos", 'slug')

