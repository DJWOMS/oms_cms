from django.urls import path
from . import views

urlpatterns = [
    path('pages-list/', views.PagesListApi.as_view(), name='pages_list_api'),
    path('pages/<int:id>', views.PagesRetrieveWithId.as_view(), name='pages_retrieve_api'),
    path('pages-delete-update/<int:id>/', views.PagesDeleteUpdateWithId.as_view(), name='pages_delete_update_api'),
    path('pages-create/', views.PagesCreate.as_view(), name='pages_create_api'),
    path('blockpage-list/', views.BlockPageListApi.as_view(), name='blockpage_list_api'),
    path('blockpage/<int:id>', views.BlockPageRetrieveWithId.as_view(), name='blockpage_retrieve_api'),
    path('blockpage-delete-update/<int:id>/', views.BlockPageDeleteUpdateWithId.as_view(), name='blockpage_delete_update_api'),
    path('blockpage-create/', views.BlockPageCreate.as_view(), name='blockpage_create'),
]
