from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from django.contrib import admin
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include(('Authentication.urls', 'authentication'), namespace='authentication')),
    # path('', include(('Dashboard.urls', 'dashboard'), namespace='dashboard')),
    path('', views.home , name='index')
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

