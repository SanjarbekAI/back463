from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from page.views import home_page_view, new_detail_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("page.urls", namespace="page"))

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
