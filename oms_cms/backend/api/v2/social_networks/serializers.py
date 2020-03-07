from rest_framework import serializers

from oms_cms.backend.social_networks.models import SocialNetworks


class SocialNetworksSerializer(serializers.ModelSerializer):
    """Сериализация социальных сетей"""
    class Meta:
        model = SocialNetworks
        fields = '__all__'


