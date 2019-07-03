from django.urls import path

from .views import *


urlpatterns = [
    path("<slug:name>/", GetLang.as_view(), name="name_lang")
]