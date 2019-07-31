from django.urls import path

from .views import *


urlpatterns = [
    path(
        'location-autocomplete/',
        LocationAutocompleteView.as_view(),
        name='location-autocomplete'
    ),
]