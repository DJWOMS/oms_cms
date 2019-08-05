from django.urls import path

from .views import *


urlpatterns = [
    path("comment-edit/<int:pk>/", EditComment.as_view(), name="edit_comment"),
    path("comment-answer/<int:pk>/", AnswerComment.as_view(), name="answer_comment"),
    path("comment-del/<int:pk>/", DeleteComment.as_view(), name="delete_comment"),
    path("<slug:category>/<slug:post>/", PostDetail.as_view(), name="new-detail"),
    path("<slug:slug>/", PostView.as_view(), name="list-news"),
    path("", PostView.as_view(), name="all-news"),
]
