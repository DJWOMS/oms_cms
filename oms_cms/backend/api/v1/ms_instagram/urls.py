from django.urls import path
from . import views

urlpatterns = [
    path('', views.PhotoListInstagram.as_view()),
    path('followers/', views.FollowInstagram.as_view()),
]