from django.urls import path
from . import views

urlpatterns = [
    path('partners-list/', views.PartnersListApi.as_view(), name='partners_list_api'),
    path('partners-retrieve-delete-update/<int:id>', views.PartnersDeleteUpdateRetrieveWithId.as_view(),
         name='partners_retrieve_delete_update_api'),
    path('partners-create/', views.PartnersCreate.as_view(), name='partners_create_api'),
]
