from django.urls import path

from .views import *


urlpatterns = [
    # path("create-comment/<int:pk>/", CommentCreate.as_view(), name="comment-create"),
    path("edit-comment/<int:pk>/", EditComment.as_view(), name="edit_comment"),
    path("answer-comment/<int:pk>/", AnswerComment.as_view(), name="answer_comment"),
    path("<slug:post>/delete-comment/<int:pk>/", DeleteComment.as_view(), name="delete_comment"),
    path("<slug:category>/<slug:post>/", PostDetail.as_view(), name="new-detail"),
    path("<slug:slug>/", PostView.as_view(), name="list-news"),
    path("", PostView.as_view(), name="all-news"),
]
