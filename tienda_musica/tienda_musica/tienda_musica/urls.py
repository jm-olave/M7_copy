"""
URL configuration for tienda_musica project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tienda_gestion.views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('crear_artista/', crear_artista, name='crear-artista'),
    path('exportar/', exportar_artistas, name='exportar'),
    path('consulta/', consultar_artistas_album, name='consulta'),
    path('email/', enviar_correo, name='envio_correo'),
    path('archivo/', subida_archivo, name = 'subir_archivo'),
    path('', index, name='index'),
    path('votar/<int:item_id>/', votar_item, name='votar')
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

