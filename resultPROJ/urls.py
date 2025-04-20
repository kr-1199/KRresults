from django.contrib import admin
from django.urls import path
from resultAPP.views import studentRESULT
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', studentRESULT, name="studentRESULT"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)