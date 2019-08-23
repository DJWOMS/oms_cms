from django.urls import path

from .views import *

app_name = "pages"
urlpatterns = [
    # path('<slug:slug>/', Page.as_view(), name="page_slug"),
    path('', Page.as_view(), name="page"),
]
