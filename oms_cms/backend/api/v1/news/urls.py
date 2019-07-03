from django.urls import path
from . import views

urlpatterns = [
    path('category-list/', views.CategoryList.as_view()),
    path("<slug:category_slug>/", views.PostList.as_view()),
    path("post/<int:id>/", views.PostDetail.as_view()),
]