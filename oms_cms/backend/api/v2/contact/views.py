from rest_framework import generics, permissions
from rest_framework import filters as filters_rf
from django_filters import rest_framework as filters

from oms_cms.backend.contact.models import Contact, ContactFields, ContactSocNet, Feedback
from .serializers import ContactSerializer, ContactFieldsSerializer, ContactDeleteUpdateCreateSerializer, \
    ContactSocNetSerializer, ContactSocNetCreateDeleteUpdateSerializer, FeedbackSerializer


class ContactListApi(generics.ListAPIView):
    """Список всех контактов"""
    permission_classes = [permissions.AllowAny]
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    filter_backends = [filters.DjangoFilterBackend,
                       filters_rf.SearchFilter,
                       filters_rf.OrderingFilter]
    filter_fields = ('id', 'lang')
    search_fields = ['id', 'slug', 'name', 'description']
    ordering = ['id']


class ContactRetrieveApi(generics.RetrieveAPIView):
    """Просмотр отдельного контакта"""
    permission_classes = [permissions.AllowAny]
    queryset = Contact.objects.all()
    lookup_field = 'id'
    serializer_class = ContactSerializer


class ContactDeleteUpdateApi(generics.RetrieveUpdateDestroyAPIView):
    """Изменение и удаление контактов"""
    permission_classes = [permissions.DjangoModelPermissions]
    queryset = Contact.objects.all()
    lookup_field = 'id'
    serializer_class = ContactDeleteUpdateCreateSerializer


class ContactCreateApi(generics.CreateAPIView):
    """Создание контакта"""
    permission_classes = [permissions.DjangoModelPermissions]
    queryset = Contact.objects.none()
    serializer_class = ContactDeleteUpdateCreateSerializer


class ContactFieldsListApi(generics.ListAPIView):
    """Список всех полей контактов"""
    permission_classes = [permissions.AllowAny]
    queryset = ContactFields.objects.all()
    serializer_class = ContactFieldsSerializer
    filter_backends = [filters.DjangoFilterBackend,
                       filters_rf.SearchFilter,
                       filters_rf.OrderingFilter]
    filter_fields = ('id', 'contact')
    search_fields = ['id', 'text', 'text_two']
    ordering = ['id']


class ContactFieldsRetrieveApi(generics.RetrieveAPIView):
    """Просмотр отдельного поля контакта"""
    permission_classes = [permissions.AllowAny]
    queryset = ContactFields.objects.all()
    lookup_field = 'id'
    serializer_class = ContactFieldsSerializer


class ContactFieldsDeleteUpdateApi(generics.RetrieveUpdateDestroyAPIView):
    """Изменение и удаление полей контактов"""
    permission_classes = [permissions.DjangoModelPermissions]
    queryset = ContactFields.objects.all()
    lookup_field = 'id'
    serializer_class = ContactFieldsSerializer


class ContactFieldsCreateApi(generics.CreateAPIView):
    """Создание поля контакта"""
    permission_classes = [permissions.DjangoModelPermissions]
    queryset = ContactFields.objects.none()
    serializer_class = ContactFieldsSerializer


class ContactSocNetListApi(generics.ListAPIView):
    """Список всех  соц. сетей"""
    permission_classes = [permissions.AllowAny]
    queryset = ContactSocNet.objects.all()
    serializer_class = ContactSocNetSerializer
    filter_backends = [filters.DjangoFilterBackend,
                       filters_rf.OrderingFilter]
    filter_fields = ('id', 'contact_soc', 'link')
    ordering = ['id']


class ContactSocNetRetrieveApi(generics.RetrieveAPIView):
    """Просмотр отдельной соц. сети"""
    permission_classes = [permissions.AllowAny]
    queryset = ContactSocNet.objects.all()
    lookup_field = 'id'
    serializer_class = ContactSocNetSerializer


class ContactSocNetDeleteUpdateApi(generics.RetrieveUpdateDestroyAPIView):
    """Изменение и удаление соц. сети"""
    permission_classes = [permissions.DjangoModelPermissions]
    queryset = ContactSocNet.objects.all()
    lookup_field = 'id'
    serializer_class = ContactSocNetCreateDeleteUpdateSerializer


class ContactSocNetCreateApi(generics.CreateAPIView):
    """Создание соц. сети"""
    permission_classes = [permissions.DjangoModelPermissions]
    queryset = ContactSocNet.objects.none()
    serializer_class = ContactSocNetCreateDeleteUpdateSerializer


class FeedbackListApi(generics.ListAPIView):
    """Список всех сообщений обратной связи"""
    permission_classes = [permissions.DjangoModelPermissions]
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    filter_backends = [filters.DjangoFilterBackend,
                       filters_rf.SearchFilter,
                       filters_rf.OrderingFilter]
    filter_fields = ('id', 'date')
    search_fields = ['id', 'full_name', 'email', 'phone', 'subject', 'message']
    ordering = ['id']


class FeedbackRetrieveUpdateDestroyApi(generics.RetrieveUpdateDestroyAPIView):
    """Просмотр, изменение и удаление сообщений обратной связи"""
    permission_classes = [permissions.DjangoModelPermissions]
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    lookup_field = 'id'


class FeedbackCreateApi(generics.CreateAPIView):
    """Создание сообщения обратной связи"""
    permission_classes = [permissions.AllowAny]
    queryset = Feedback.objects.none()
    serializer_class = FeedbackSerializer
