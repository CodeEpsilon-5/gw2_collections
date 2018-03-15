from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('builds/', include('builds.urls')),
    path('admin/', admin.site.urls),
    path(r'tinymce/', include('tinymce.urls')),
    path(r'djrichtextfield/', include('djrichtextfield.urls'))
]