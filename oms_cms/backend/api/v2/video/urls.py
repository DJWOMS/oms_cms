from django.urls import path
from . import views

urlpatterns = [
    path('video-list/', views.VideoListApi.as_view(), name='video_list_api'),

]
