from django.urls import path

from .views import get_page

app_name = "pages"
urlpatterns = [
    path('<path:url>', get_page, name="page"),
]
