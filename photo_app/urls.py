from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from.import views

urlpatterns = [
    path('', views.index),
    path('blog/', views.blog, name='post-list'),
    path('search/', views.search, name='search'),
    path('post/<id>/' , views.post, name='post-detail'),
] 
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)