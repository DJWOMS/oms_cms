from django.urls import path
from . import views

urlpatterns = [
    path('contact-list/', views.ContactListApi.as_view(), name='contact_list_api'),
    path('contact/<int:id>/', views.ContactRetrieveApi.as_view(), name='contact_api'),
    path('contact-delete-update/<int:id>/', views.ContactDeleteUpdateApi.as_view(),
         name='contact_delete_update_api'),
    path('contact-create/', views.ContactCreateApi.as_view(), name='contact_create_api'),
    path('contact-fields-list/', views.ContactFieldsListApi.as_view(), name='contact_fields_list_api'),
    path('contact-fields/<int:id>/', views.ContactFieldsRetrieveApi.as_view(), name='contact_fields_api'),
    path('contact-fields-delete-update/<int:id>/', views.ContactFieldsDeleteUpdateApi.as_view(),
         name='contact_fields_delete_update_api'),
    path('contact-fields-create/', views.ContactFieldsCreateApi.as_view(), name='contact_fields_create_api'),
    path('contact-soc-net-list/', views.ContactSocNetListApi.as_view(), name='contact_soc_net_list_api'),
    path('contact-soc-net/<int:id>/', views.ContactSocNetRetrieveApi.as_view(), name='contact_soc_net_api'),
    path('contact-soc-net-delete-update/<int:id>/', views.ContactSocNetDeleteUpdateApi.as_view(),
         name='contact_soc_net_delete_update_api'),
    path('contact-soc-net-create/', views.ContactSocNetCreateApi.as_view(), name='contact_soc_net_create_api'),
    path('feedback-list/', views.FeedbackListApi.as_view(), name='feedback_list_api'),
    path('feedback-retrieve-delete-update/<int:id>/', views.FeedbackRetrieveUpdateDestroyApi.as_view(),
         name='feedback_delete_update_api'),
    path('feedback-create/', views.FeedbackCreateApi.as_view(), name='feedback_create_api'),
]
