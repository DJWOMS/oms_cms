from django.urls import path, include

urlpatterns = [
    # API
    # path('api/v1/', include('oms_cms.backend.api.v1.urls')),
    path('lang/', include('oms_cms.backend.languages.urls')),
    path('<slug:lang>/news/', include('oms_cms.backend.news.urls')),
    path('contact/', include('oms_cms.backend.contact.urls')),
    path('search/', include('oms_cms.backend.search.urls')),
    path('', include('oms_cms.backend.pages.urls')),
]
