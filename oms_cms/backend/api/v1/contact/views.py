from rest_framework import generics, permissions

from oms_cms.backend.contact.models import ContactFields, Contact
from .serializers import (FeedbackPhoneSerializer,
                          ContactFieldsSerializer, ContactListSerializer, FeedbackPhoneEmailSerializer)


class CreateFeedback(generics.CreateAPIView):
    """Добавление сообщения обратной связи"""
    permission_classes = [permissions.AllowAny]
    serializer_class = FeedbackPhoneSerializer


class CreatePhoneEmailFeedback(generics.CreateAPIView):
    """Добавление сообщения обратной связи"""
    permission_classes = [permissions.AllowAny]
    serializer_class = FeedbackPhoneEmailSerializer


class ContactList(generics.ListAPIView):
    """Список контактов"""
    permission_classes = [permissions.AllowAny]
    queryset = Contact.objects.all()
    serializer_class = ContactListSerializer


class ContactFieldsList(generics.ListAPIView):
    """Список полей контактов"""
    permission_classes = [permissions.AllowAny]
    lookup_field = 'contact'
    queryset = ContactFields.objects.all()
    serializer_class = ContactFieldsSerializer

    # def get_queryset(self):
    #     return ContactFields.objects.filter(contact__id=self.request.get("id"))


