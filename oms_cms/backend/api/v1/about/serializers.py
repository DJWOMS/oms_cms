from rest_framework import serializers

from oms_cms.backend.about.models import AboutBlock
from oms_cms.backend.api.v1.photologue.serializers import GallerySerializer


class AboutBlockSerializer(serializers.ModelSerializer):
    """О нас"""
    slider = GallerySerializer()

    class Meta:
        model = AboutBlock
        fields = ("title",
                  "desc",
                  "slider"
                  )
