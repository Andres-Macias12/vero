# barrio/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from comercios.views import pagina_principal

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', pagina_principal, name='pagina-principal'),  # Página principal
    path('comercios/', include('comercios.urls')),  # Rutas de comercios
]

# Servir archivos multimedia en modo desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
