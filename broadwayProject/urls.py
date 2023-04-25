from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    # path("", include('myapp.urls')),
    path("c/", include('classbased.urls')),
    path("api/", include('api.urls')),
    path("api/crud/", include('api_crud.urls')),
    path("", include('account.urls')),
    path("", include('crud.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

