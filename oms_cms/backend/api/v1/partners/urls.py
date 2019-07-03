from django.urls import path
from . import views

urlpatterns = [
    path('', views.PartnersList.as_view()),
]
