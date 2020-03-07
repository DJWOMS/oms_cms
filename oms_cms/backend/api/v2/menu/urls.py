from django.urls import path
from . import views

urlpatterns = [
    path('menu-list/', views.MenuListApi.as_view(), name='menu_list_api'),
    path('menu/<int:id>/', views.MenuRetrieveWithId.as_view(), name='menu_api'),
    path('menu-delete-update/<int:id>/', views.MenuDeleteUpdateWithId.as_view(), name='menu_delete_update_api'),
    path('menu-create/', views.MenuCreate.as_view(), name='menu_create_api'),
    path('menu-create/', views.MenuCreate.as_view(), name='menu_create_api'),
    path('menuitem-list', views.MenuItemListApi.as_view(), name='menuitem_list_api'),
    path('menuitem/<int:id>/', views.MenuItemRetrieveWithId.as_view(), name='menuitem_api'),
    path('menuitem-delete-update/<int:id>/', views.MenuItemDeleteUpdateWithId.as_view(),
         name='menuitem_delete_update_api'),
    path('menuitem-create/', views.MenuItemCreate.as_view(), name='menuitem_create_api'),
]
