from django.urls import path

from .views import *

urlpatterns = [
    path('<slug:lang>/<slug:slug>/', Page.as_view(), name="page_slug_lang"),
    path('<slug:slug>/', Page.as_view(), name="page_slug"),
    path('', Page.as_view(), name="page"),
]
