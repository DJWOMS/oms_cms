from rest_framework import serializers

from oms_cms.backend.oms_seo.models import Seo, ConnectSSModel, CounterForSite
from oms_cms.backend.api.v2.menu.serializers import ContentTypeSerializer


class SeoSerializer(serializers.ModelSerializer):
    """Сериализация Email для рассылки"""
    content_type = ContentTypeSerializer(read_only=True)
    class Meta:
        model = Seo
        fields = ('id', 'title_page', 'description_page', 'object_id', 'content_type')


class SeoCreateSerializer(serializers.ModelSerializer):
    """Сериализация Email для рассылки"""
    class Meta:
        model = Seo
        fields = '__all__'


class ConnectSSModelSerializer(serializers.ModelSerializer):
    """Сериализация подключений ПС"""
    class Meta:
        model = ConnectSSModel
        fields = '__all__'


class CounterForSiteSerializer(serializers.ModelSerializer):
    """Сериализация счетчиков"""
    class Meta:
        model = CounterForSite
        fields = '__all__'


