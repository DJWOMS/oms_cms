from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>/', views.ContactFieldsList.as_view()),
    path('feedback/phone/', views.CreateFeedback.as_view()),
    path('feedback/phone-email/', views.CreatePhoneEmailFeedback.as_view()),
    path('', views.ContactList.as_view()),
]