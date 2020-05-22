from django.urls import path
from . import views

urlpatterns = [
    path('languages-list/', views.AbstractLangListApi.as_view(), name='languages_list_api'),
    # path('partners-retrieve-delete-update/<int:id>', views.PartnersDeleteUpdateRetrieveWithId.as_view(),
    #      name='partners_retrieve_delete_update_api'),
    # path('partners-create/', views.PartnersCreate.as_view(), name='partners_create_api'),
]
