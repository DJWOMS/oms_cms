from django.urls import path
from . import views

urlpatterns = [
    path('social-networks-list/', views.SocialNetworksListApi.as_view(), name='social_networks_list_api'),
    path('social-networks-retrieve-delete-update/<int:id>', views.SocialNetworksDeleteUpdateRetrieveWithId.as_view(),
         name='social_networks_retrieve_delete_update_api'),
    path('social-networks-create/', views.SocialNetworksCreate.as_view(), name='social_networks_create_api'),
]
