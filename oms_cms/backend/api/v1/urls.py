from django.urls import path, re_path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Oms API",
        default_version='v1',
        description="Test description",
        # terms_of_service="https://www.google.com/policies/terms/",
        # contact=openapi.Contact(email="contact@snippets.local"),
        # license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('news/', include('oms_cms.backend.api.v1.news.urls')),
    # path('contact/', include('oms_cms.backend.api.v1.contact.urls')),
    # path('gallery/', include('oms_cms.backend.api.v1.photologue.urls')),
    # path('video/', include('oms_cms.backend.api.v1.video.urls')),
    # path('info-block/', include('oms_cms.backend.api.v1.info_block.urls')),
    # path('partners/', include('oms_cms.backend.api.v1.partners.urls')),

    # re_path('swagger(?P<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0),
    #         name='schema-json'),
    # path('swagger/', schema_view.with_ui('swagger', cache_timeout=0),
    #      name='schema-swagger-ui'),
    # path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
