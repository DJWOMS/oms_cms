from django.urls import path
from . import views

urlpatterns = [
    path('social-app-list/', views.SocialAppListApi.as_view(), name='social_app_list_api'),
    path('social-app/<int:id>/', views.SocialAppRetrieveDeleteUpdateApi.as_view(),
         name='social_app_retrieve_delete_update_api'),
    path('social-app-create/', views.SocialAppCreateApi.as_view(), name='social_app_create_api'),
    path('social-account-list/', views.SocialAccountListApi.as_view(), name='social_account_list_api'),
    path('social-account/<int:id>/', views.SocialAccountRetrieveDeleteUpdateApi.as_view(),
         name='social_account_retrieve_delete_update_api'),
    path('social-account-create/', views.SocialAccountCreateApi.as_view(), name='social_account_create_api'),
    path('social-token-list/', views.SocialTokenListApi.as_view(), name='social_token_list_api'),
    path('social-token/<int:id>/', views.SocialTokenRetrieveDeleteUpdateApi.as_view(),
         name='social_token_retrieve_delete_update_api'),
    path('social-token-create/', views.SocialTokenCreateApi.as_view(), name='social_token_create_api'),
]
