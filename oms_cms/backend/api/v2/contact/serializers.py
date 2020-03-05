from rest_framework import serializers

from oms_cms.backend.contact.models import Contact, ContactFields, ContactSocNet, Feedback
from oms_cms.backend.api.v2.social_networks.serializers import SocialNetworksSerializer




class ContactFieldsSerializer(serializers.ModelSerializer):
    """Сериализация полей контактов"""
    class Meta:
        model = ContactFields
        fields = '__all__'


class ContactSocNetSerializer(serializers.ModelSerializer):
    """Сериализация социальных сетей"""
    link = SocialNetworksSerializer()
    class Meta:
        model = ContactSocNet
        fields = ('id', 'contact_soc', 'your_id', 'link')


class ContactSocNetCreateDeleteUpdateSerializer(serializers.ModelSerializer):
    """Сериализация социальных сетей"""
    class Meta:
        model = ContactSocNet
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    """Сериализация контактов"""
    contact_field = ContactFieldsSerializer(read_only=True, many=True)
    soc_net = ContactSocNetSerializer(many=True)
    class Meta:
        model = Contact
        fields = ('id', 'lang', 'slug', 'name', 'description', 'map', 'contact_field', 'soc_net')


class ContactDeleteUpdateCreateSerializer(serializers.ModelSerializer):
    """Сериализация контактов"""
    class Meta:
        model = Contact
        fields = '__all__'


class FeedbackSerializer(serializers.ModelSerializer):
    """Сериализация сообщений обратной связи"""
    class Meta:
        model = Feedback
        fields = '__all__'


