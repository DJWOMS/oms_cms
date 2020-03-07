from django.urls import path
from . import views

urlpatterns = [
    path('tags-list/', views.TagsListApi.as_view()),                                        # Список тегов
    path('tags/<int:id>/', views.TagRetrieveWithId.as_view()),                              # Просмотр информации о теге (ID)
    path('tags-delete-update/<int:id>/', views.TagsDeleteUpdateWithId.as_view()),           # Удалить/изменить тег (ID)
    path('tag-create/', views.TagsCreate.as_view()),                                        # Создание тега
    path('category-list/', views.CategoryListApi.as_view()),                                # Список категорий
    path('category/<int:id>/', views.CategoryRetrieveWithId.as_view()),                     # Просмотр информации о категории (ID)
    path('category-delete-update/<int:id>/', views.CategoryDeleteUpdateWithId.as_view()), #FIX slug/url input   # Удалить/изменить категорию (ID)
    path('category-create/', views.CategoryCreate.as_view()),            #FIX slug/url input                   # Создание категории
    path('post-list/', views.PostList.as_view()),                                           # Список статей
    path('post/<int:id>/', views.PostRetrieveWithId.as_view()),                             # Просмотр информации о новости (ID)
    path('post-delete-update/<int:id>/', views.PostDeleteUpdateWithId.as_view()),  #FIX slug/url input         # Удалить/изменить новость (ID)
    path('post-create/', views.PostCreate.as_view()),                  #FIX slug/url input                     # Создание новости
]
