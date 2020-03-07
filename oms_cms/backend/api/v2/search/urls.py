from django.urls import path
from . import views

urlpatterns = [
    path('spysearch-list/', views.SpySearchListApi.as_view(), name='spysearch_list_api'),

]
