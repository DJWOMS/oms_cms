from django.urls import path
from . import views

urlpatterns = [
    path('info-block-list/', views.InfoBlockListApi.as_view(), name='info_block_list_api'),
    path('info-block/<int:id>', views.InfoBlockRetrieveApi.as_view(), name='info_block_api'),
    path('info-block-delete-update/<int:id>/', views.InfoBlockDeleteUpdateWithId.as_view(),
         name='info_block_delete_update_api'),
    path('info-block-create/', views.InfoBlockCreate.as_view(), name='info_block_create_api'),
]
