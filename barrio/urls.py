# barrio/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from comercios.views import pagina_principal
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', pagina_principal, name='pagina-principal'),  # Página principal
    path('comercios/', include('comercios.urls')),  # Rutas de comercios
    path('login/', auth_views.LoginView.as_view(), name='login'), #Ruta para login
    path('logout/', auth_views.LogoutView.as_view(), name='logout'), #Ruta para el logout
]   

# Servir archivos multimedia en modo desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
