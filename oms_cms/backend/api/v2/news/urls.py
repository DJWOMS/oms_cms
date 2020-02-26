from django.urls import path
from . import views

urlpatterns = [
    path('tags-list/', views.TagsListApi.as_view()),                                        # Список тегов
    path('tags/<int:id>/', views.TagRetrieveWithId.as_view()),                              # Просмотр информации о теге (ID)
    path('tags/<slug:slug>/', views.TagRetrieveWithSlug.as_view()),                         # Просмотр информации о теге (slug)
    path('tags-delete-update/<int:id>/', views.TagsDeleteUpdateWithId.as_view()),           # Удалить/изменить тег (ID)
    path('tag-create/', views.TagsCreate.as_view()),                                        # Создание тега
    path('category-list/', views.CategoryListApi.as_view()),                                # Список категорий
    path('category/<int:id>/', views.CategoryRetrieveWithId.as_view()),                     # Просмотр информации о категории (ID)
    path('category/<slug:slug>/', views.CategoryRetrieveWithSlug.as_view()),                # Просмотр информации о категории (slug)
    path('category-delete-update/<int:id>/', views.CategoryDeleteUpdateWithId.as_view()), #FIX slug/url input   # Удалить/изменить категорию (ID)
    path('category-create/', views.CategoryCreate.as_view()),            #FIX slug/url input                   # Создание категории
    path('post-list/', views.PostList.as_view()),                                           # Список статей
    path('post/<int:id>/', views.PostRetrieveWithId.as_view()),                             # Просмотр информации о новости (ID)
    path('post/<slug:slug>/', views.PostRetrieveWithSlug.as_view()),                        # Просмотр информации о новости (slug)
    path('post-delete-update/<int:id>/', views.PostDeleteUpdateWithId.as_view()),  #FIX slug/url input         # Удалить/изменить новость (ID)
    path('post-delete-update/<slug:slug>/', views.PostDeleteUpdateWithSlug.as_view()), #FIX slug/url input     # Удалить/изменить новость (slug)
    path('post-create/', views.PostCreate.as_view()),                  #FIX slug/url input                     # Создание новости
]
