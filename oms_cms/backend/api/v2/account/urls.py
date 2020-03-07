from django.urls import path
from . import views

urlpatterns = [
    path('email-address-list/', views.EmailAddressListApi.as_view(), name='email_address_list_api'),
    path('email-address/<int:id>', views.EmailAddressRetrieveeleteUpdateApi.as_view(), name='email_address_api'),
    path('email-address-create/', views.EmailAddressCreateApi.as_view(), name='email_address_create_api'),
]
