from django.urls import path

from .views import *

app_name = "news"
urlpatterns = [
    path("tag/<slug:tag>/", PostView.as_view(), name="tag-news"),
    path("<slug:category>/<slug:post>/", PostDetail.as_view(), name="new-detail"),
    path("<slug:slug>/", PostView.as_view(), name="list-news"),
    path("", PostView.as_view(), name="all-news"),
]
