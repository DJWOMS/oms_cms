"""CMS - DJWOMS
"""
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

import oms_cms.backend.urls
from oms_cms.config.base import sitemaps

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
    path('accounts/', include('allauth.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

urlpatterns += oms_cms.backend.urls.urlpatterns
urlpatterns += [
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type='text/plain')),
]


admin.site.site_title = "OMS CMS"
admin.site.site_header = "OMS CMS"

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
