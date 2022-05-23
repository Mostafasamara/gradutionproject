from django.contrib import admin
from django.conf.urls import include
from django.urls import re_path

from django.urls import path
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from rest_auth.views import PasswordResetConfirmView
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView


API_TITLE = 'Pastebin API'
API_DESCRIPTION = 'A Web API for creating and viewing highlighted code snippets.'
schema_view = get_schema_view(title=API_TITLE)

urlpatterns = [

    re_path('^admin/', admin.site.urls),
    re_path(r'^api-auth/', include('rest_auth.urls')),
    re_path(r'^', include('django.contrib.auth.urls')),

    re_path(r'', include('project.urls')),
    re_path(r'^favicon\.ico$',RedirectView.as_view(url='/static/images/favicon.ico')),
    re_path(r'^schema/$', schema_view),
    re_path(r'^docs/', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION))
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
