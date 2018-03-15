from django.urls import include, path, re_path
from django.contrib import admin
from django.views.generic.base import RedirectView

urlpatterns = [
    path('builds/', include('builds.urls'), name='builds'),
    path('admin/', admin.site.urls),
    path(r'tinymce/', include('tinymce.urls')),
    path(r'djrichtextfield/', include('djrichtextfield.urls')),
    path(r'', RedirectView.as_view(pattern_name='index'))
]
