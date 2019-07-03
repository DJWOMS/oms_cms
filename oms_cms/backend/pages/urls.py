from django.urls import path

from .views import *

urlpatterns = [
    # path('<path:url>', Page.as_view(), name="page"),
    path('', Page.as_view(), name="page"),
    path('<slug:lang>/', Page.as_view(), name="page"),
    path('<slug:lang>/<slug:slug>/', Page.as_view(), name="page")
]