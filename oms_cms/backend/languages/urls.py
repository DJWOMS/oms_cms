from django.urls import path

from .views import *

app_name = "languages"
urlpatterns = [
    path("", GetLang.as_view(), name="set_lang")
]