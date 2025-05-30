from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

admin.site.site_header = 'STOREAPP-API'

urlpatterns = [
    path('admin/', admin.site.urls),
     path('api/', include('api.urls')),
    # path('user/', include('users.urls')),
    path('api-auth/', include('rest_framework.urls'))
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )