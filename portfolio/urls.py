from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns

from . import views

urlpatterns = [
    path('', views.home , name='index'),
    path('register', views.registerUser, name="register"),
    path('login',views.login_user,name="login"),
    path('logout',views.logout_user,name="logout"),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

