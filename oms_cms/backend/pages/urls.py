from django.urls import path

from .views import *

app_name = "pages"
urlpatterns = [
    path('<path:url>', page, name="page"),
]
