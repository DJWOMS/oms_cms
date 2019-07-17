from oms_cms.backend.news.sitemap import PostSitemap
from oms_cms.backend.pages.sitemap import PagesSitemap

sitemaps = {
    'news': PostSitemap,
    'pages': PagesSitemap,
}