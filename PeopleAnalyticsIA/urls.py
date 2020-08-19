from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('painel/', admin.site.urls),
    path('', include('users.urls'))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# How there's no media server to give  static files, I'm get own my root as
# default of machine