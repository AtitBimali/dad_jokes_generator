
from django.contrib import admin
from django.urls import path,include
from django.conf import settings #add this
from django.conf.urls.static import static 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('api.urls')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
