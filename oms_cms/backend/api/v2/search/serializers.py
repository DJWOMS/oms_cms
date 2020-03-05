from rest_framework import serializers

from oms_cms.backend.search.models import SpySearch


class SpySearchSerializer(serializers.ModelSerializer):
    """Сериализация SpySearch"""
    class Meta:
        model = SpySearch
        fields = '__all__'


