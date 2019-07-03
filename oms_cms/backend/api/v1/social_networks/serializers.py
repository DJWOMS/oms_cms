from rest_framework import serializers

from oms_cms.backend.social_networks.models import SocialNetworks


class SocialNetworksSerializer(serializers.ModelSerializer):
    """Соц. сети"""
    class Meta:
        model = SocialNetworks
        fields = ("title", "icon_ui", "icon", "link")