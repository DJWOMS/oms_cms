from django.urls import path

from .views import *


urlpatterns = [
    path("<slug:category>/<slug:post>/", PostDetail.as_view(), name="new-detail"),
    path("<slug:slug>/", News.as_view(), name="list-news"),
    path("", AllNews.as_view(), name="all-news"),
]