from rest_framework import serializers
from oms_cms.backend.api.v1.social_networks.serializers import SocialNetworksSerializer
# from oms_cms.backend.social_networks.models import SocialNetworks

from oms_cms.backend.contact.models import (Feedback, ContactFields, ContactSocNet, Contact)


class FeedbackPhoneSerializer(serializers.ModelSerializer):
    """Обратная связь по тел."""
    class Meta:
        model = Feedback
        fields = ("full_name", "tel", "message", "section")


class FeedbackPhoneEmailSerializer(serializers.ModelSerializer):
    """Обратная связь по тел. & email"""
    class Meta:
        model = Feedback
        fields = ("full_name", "tel", "email", "section")


class ContactSocNetSerializer(serializers.ModelSerializer):
    """Соцю сети контактов"""
    link = SocialNetworksSerializer()

    class Meta:
        model = ContactSocNet
        fields = ("id", "contact_soc", "your_id", "link")


class ContactSerializer(serializers.ModelSerializer):
    """Контакты"""
    # soc_net = ContactSocNetSerializer()
    # contact_soc = serializers.PrimaryKeyRelatedField(many=True, queryset=ContactSocNet.objects.all())

    class Meta:
        model = Contact
        fields = ("id", "name", "desk_cont", "map", "slug")


class ContactFieldsSerializer(serializers.ModelSerializer):
    """Поля контактов"""
    contact = ContactSerializer()

    class Meta:
        model = ContactFields
        fields = ("id", "text", "text_two", "icon_ui", "icon", "type", "contact")


class ContactFieldsListSerializer(serializers.ModelSerializer):
    """Список полей контактов"""

    class Meta:
        model = ContactFields
        fields = ("id", "text", "text_two", "icon_ui", "icon", "type",)


class ContactListSerializer(serializers.ModelSerializer):
    """Список контактов"""
    soc_net = ContactSocNetSerializer(many=True, read_only=True)
    contact_field = ContactFieldsListSerializer(many=True, read_only=True)

    class Meta:
        model = Contact
        fields = ("id", "name", "section", "desk_cont", "map", "contact_field", "soc_net", "slug")