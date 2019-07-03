from django.urls import path

from .views import *


urlpatterns = [
    path("feedback/", FeedbackView.as_view(), name="feedback"),
    path("add-feedback/", AddFeedback.as_view(), name="add_feedback")
]