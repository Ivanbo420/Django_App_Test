from main import urls as main_app_urls
from users import urls as users_app_urls
from django.contrib import admin
from django.urls import path, include
from automax import settings
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(main_app_urls)),
    path('', include(users_app_urls)),
]

urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])