from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.settings.urls')),
    path('team/', include('apps.team.urls')),
    path('course/', include('apps.courses.urls')),
    path('users/', include('apps.users.urls')),
    path('ckeditor/',include('ckeditor_uploader.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)