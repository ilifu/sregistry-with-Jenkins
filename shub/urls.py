'''

Copyright (C) 2017-2019 Vanessa Sochat.

This Source Code Form is subject to the terms of the
Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed
with this file, You can obtain one at http://mozilla.org/MPL/2.0/.

'''

from importlib import import_module

from django.conf import settings
from django.conf.urls import (include, url)
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap, index
from shub.apps.api import urls as api_urls
from shub.apps.base import urls as base_urls
from shub.apps.library import urls as library_urls
from shub.apps.main import urls as main_urls
from shub.apps.users import urls as user_urls
from shub.apps.base.sitemap import (
    CollectionSitemap, 
    ContainerSitemap
)

from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls

# Documentation URL
API_TITLE = 'Singularity Registry API'
API_DESCRIPTION = 'Open Source Container Registry API'
schema_view = get_schema_view(title=API_TITLE)

# Configure custom error pages
handler404 = 'shub.apps.base.views.handler404'
handler500 = 'shub.apps.base.views.handler500'

# Sitemaps
sitemaps = {"containers": ContainerSitemap,
            "collections": CollectionSitemap}

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(base_urls)),
    url(r'^api/', include(api_urls)),
    url(r'^v1/', include(library_urls)),  # Sylabs library API
    url(r'^api/schema/$', schema_view),
    url(r'^api/docs/', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION)),
    url(r'^', include(main_urls)),
    url(r'^', include(user_urls)),
    url(r'^sitemap\.xml$', index, {'sitemaps': sitemaps}, name="sitemap"),
    url(r'^sitemap-(?P<section>.+)\.xml$', sitemap, {'sitemaps': sitemaps}),
    url(r'^django-rq/', include('django_rq.urls'))
]

# Load URLs for any enabled plugins
for plugin in settings.PLUGINS_ENABLED:
    urls_module = 'shub.plugins.' + plugin + '.urls'
    plugin_urls = import_module(urls_module)
    url_regex = '^' + plugin + '/'
    urlpatterns.append(url(url_regex, include(plugin_urls)))
