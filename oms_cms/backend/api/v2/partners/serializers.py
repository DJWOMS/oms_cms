from rest_framework import serializers

from oms_cms.backend.partners.models import Partners


class PartnersSerializer(serializers.ModelSerializer):
    """Сериализация партнеров"""
    class Meta:
        model = Partners
        fields = '__all__'


