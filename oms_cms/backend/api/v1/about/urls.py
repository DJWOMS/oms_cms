from django.urls import path
from . import views

urlpatterns = [
    path('', views.AboutBlockList.as_view()),
]
