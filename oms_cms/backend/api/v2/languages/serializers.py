from rest_framework import serializers

from oms_cms.backend.languages.models import AbstractLang


class AbstractLangSerializer(serializers.ModelSerializer):
    """Сериализация модели языка"""
    class Meta:
        model = AbstractLang
        fields = '__all__'

