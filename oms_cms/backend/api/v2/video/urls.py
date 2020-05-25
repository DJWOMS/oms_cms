from django.urls import path
from . import views

urlpatterns = [
    path('video-list/', views.VideoListApi.as_view(), name='video_list_api'),
    path('video/<int:id>/', views.VideoRetrieveApi.as_view(), name='video_retrieve_api'),
    path('video-delete-update/<int:id>/', views.VideoUpdateDeleteApi.as_view(), name='video_delete_update_api'),
    path('video-create/', views.VideoCreateApi.as_view(), name='video_create_api'),

]
