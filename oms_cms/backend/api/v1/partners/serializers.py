from rest_framework import serializers

from oms_cms.backend.partners.models import Partners


class PartnersSerializer(serializers.ModelSerializer):
    """Партнеры"""
    picture = serializers.URLField(read_only=True, source='picture.url')

    class Meta:
        model = Partners
        fields = ("picture",
                  "link"
                  )
