from django.urls import path
from . import views

urlpatterns = [
    path('email-feedback-list/', views.EmailsFeedbackListApi.as_view(), name='email_feedback_list_api'),
    path('email-feedback-retrieve-delete-update/<int:id>', views.EmailsFeedbackDeleteUpdateRetrieveWithId.as_view(),
         name='email_feedback_retrieve_delete_update_api'),
    path('email-feedback-create/', views.EmailsFeedbackCreate.as_view(), name='email_feedback_create_api'),
]
