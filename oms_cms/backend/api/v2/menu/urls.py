from django.urls import path
from . import views

urlpatterns = [
    path('menu-list/', views.MenuListApi.as_view(), name='menu_list_api'),
    path('menu/<int:id>/', views.MenuRetrieveApi.as_view(), name='menu_api'),
    path('menu-delete-update/<int:id>/', views.MenuDeleteUpdateApi.as_view(), name='menu_delete_update_api'),
    path('menu-create/', views.MenuCreateApi.as_view(), name='menu_create_api'),
    path('menuitem-list/', views.MenuItemListApi.as_view(), name='menuitem_list_api'),
    path('menuitem/<int:id>/', views.MenuItemRetrieveApi.as_view(), name='menuitem_api'),
    path('menuitem-delete-update/<int:id>/', views.MenuItemDeleteUpdateApi.as_view(),
         name='menuitem_delete_update_api'),
    path('menuitem-create/', views.MenuItemCreateApi.as_view(), name='menuitem_create_api'),
]
