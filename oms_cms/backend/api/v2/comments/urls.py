from django.urls import path
from . import views

urlpatterns = [
    path('comments-list/', views.OmsCommentListApi.as_view(), name='oms_comment_list_api'),
    path('comment/<int:id>', views.OmsCommentApi.as_view(), name='oms_comment_api'),
    path('comment-delete-update/<int:id>/', views.OmsCommentDeleteUpdateWithId.as_view(),
         name='oms_comment_delete_update_api'),
    path('comment-create/', views.OmsCommentCreate.as_view(), name='oms_comment_create_api'),
]
