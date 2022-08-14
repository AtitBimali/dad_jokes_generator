from . import views
from django.urls import path
from django.conf import settings #add this
from django.conf.urls.static import static 
urlpatterns = [
    path('', views.jokes,name='jokes'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)