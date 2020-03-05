from django.urls import path
from . import views

urlpatterns = [
    path('seo-list/', views.SeoListApi.as_view(), name='seo_list_api'),
    path('seo-retrieve-delete-update/<int:id>', views.SeoDeleteUpdateRetrieveWithId.as_view(),
         name='seo_retrieve_delete_update_api'),
    path('seo-create/', views.SeoCreate.as_view(), name='seo_create_api'),
    path('connect-ss-list/', views.ConnectSSModelListApi.as_view(), name='connect_ss_list_api'),
    path('connect-ss-retrieve-delete-update/<int:id>', views.ConnectSSModelDeleteUpdateRetrieveWithId.as_view(),
         name='connect_ss_retrieve_delete_update_api'),
    path('connect-ss-create/', views.ConnectSSModelCreate.as_view(), name='connect_ss_create_api'),
    path('counter-list/', views.CounterForSiteListApi.as_view(), name='counter_list_api'),
    path('counter-retrieve-delete-update/<int:id>', views.CounterForSiteDeleteUpdateRetrieveWithId.as_view(),
         name='counter_retrieve_delete_update_api'),
    path('counter-create/', views.CounterForSiteCreate.as_view(), name='counter_create_api'),
]
