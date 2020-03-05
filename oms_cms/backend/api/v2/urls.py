from django.urls import path,  include
# from rest_framework import permissions
# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi

# schema_view = get_schema_view(
#     openapi.Info(
#         title="Oms API",
#         default_version='v1',
#         description="Test description",
#         # terms_of_service="https://www.google.com/policies/terms/",
#         # contact=openapi.Contact(email="contact@snippets.local"),
#         # license=openapi.License(name="BSD License"),
#     ),
#     public=True,
#     permission_classes=(permissions.AllowAny,),
# )

urlpatterns = [
    path('news/', include('oms_cms.backend.api.v2.news.urls')),
    path('pages/', include('oms_cms.backend.api.v2.pages.urls')),
    path('menu/', include('oms_cms.backend.api.v2.menu.urls')),
    path('video/', include('oms_cms.backend.api.v2.video.urls')),
    path('search/', include('oms_cms.backend.api.v2.search.urls')),
    path('comments/', include('oms_cms.backend.api.v2.comments.urls')),
    path('info-block/', include('oms_cms.backend.api.v2.info_block.urls')),
    path('partners/', include('oms_cms.backend.api.v2.partners.urls')),
    path('social-networks/', include('oms_cms.backend.api.v2.social_networks.urls')),
    path('utils/', include('oms_cms.backend.api.v2.utils.urls')),
    path('oms-seo/', include('oms_cms.backend.api.v2.oms_seo.urls')),
    path('contact/', include('oms_cms.backend.api.v2.contact.urls')),
    path('account/', include('oms_cms.backend.api.v2.account.urls')),
    path('socialaccount/', include('oms_cms.backend.api.v2.socialaccount.urls')),
    # path('languages/', include('oms_cms.backend.api.v2.languages.urls')),


    # re_path('swagger(?P<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0),
    #         name='schema-json'),
    # path('swagger/', schema_view.with_ui('swagger', cache_timeout=0),
    #      name='schema-swagger-ui'),
    # path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]