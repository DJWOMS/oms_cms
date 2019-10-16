from django.urls import path

from .views import *

app_name = "comments"
urlpatterns = [
    path('post/', post_comment, name='post-comment'),
    # path("comment-edit/<int:pk>/", EditCommentView.as_view(), name="edit_comment"),
    # path("comment-del/<int:pk>/", DeleteComment.as_view(), name="delete_comment")
]
