"""CMS - DJWOMS
"""
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

from oms_cms.config.base import sitemaps

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('i18n/', include('django.conf.urls.i18n')),
    # API
    # path('api/v1/', include('oms_cms.backend.api.v1.urls')),
    path('api/v2/', include('oms_cms.backend.api.v2.urls')),
]

urlpatterns += [
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type='text/plain')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    import debug_toolbar

    urlpatterns = [
                      path('__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns

urlpatterns += i18n_patterns(
    path('accounts/', include('allauth.urls')),
    path('comments/', include('django_comments.urls')),
    path('lang/', include('oms_cms.backend.languages.urls', namespace="languages")),
    path('contact/', include('oms_cms.backend.contact.urls', namespace='contact')),
    path('search/', include('oms_cms.backend.search.urls', namespace='search')),
    path('oms-comments/', include('oms_cms.backend.comments.urls', namespace='comments')),
    path('', include('oms_cms.backend.news.urls', namespace='news')),
    # path('', include('oms_cms.backend.pages.urls', namespace='pages')),
    prefix_default_language=True
)

admin.site.site_title = "OMS CMS"
admin.site.site_header = "OMS CMS"
