from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from .views import index, blog, features, single_slider, single_slider, single

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('blog', blog),
    path('features', features),
    path('single_slider', single_slider),
    path('single_slider', single_slider),
    path('single', single),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)