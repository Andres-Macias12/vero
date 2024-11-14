# comercios/urls.py
from . import views
from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    lista_comercios,  
    ComercioDetailView,
    ComercioCreateView, ComercioUpdateView, ComercioDeleteView,
    NovedadListView, NovedadDetailView,
    NovedadCreateView, NovedadUpdateView, NovedadDeleteView,
    register, get_messages, chat_view, pagina_principal
)

urlpatterns = [
    # Página principal
    path('', pagina_principal, name='pagina-principal'),

    # URLs para Comercio
    path('comercios/', lista_comercios, name='comercios'),  # Cambiado a 'comercios'
    path('comercios/<int:pk>/', ComercioDetailView.as_view(), name='comercio-detail'),
    path('comercios/crear/', ComercioCreateView.as_view(), name='comercio-create'),
    path('comercios/<int:pk>/editar/', ComercioUpdateView.as_view(), name='comercio-update'),
    path('comercios/<int:pk>/eliminar/', ComercioDeleteView.as_view(), name='comercio-delete'),

    # URLs para Novedad
    path('novedades/', NovedadListView.as_view(), name='novedades'),  # Cambiado a 'novedades'
    path('novedades/<int:pk>/', NovedadDetailView.as_view(), name='novedad-detail'),
    path('novedades/crear/', NovedadCreateView.as_view(), name='novedad-create'),
    path('novedades/<int:pk>/editar/', NovedadUpdateView.as_view(), name='novedad-update'),
    path('novedades/<int:pk>/eliminar/', NovedadDeleteView.as_view(), name='novedad-delete'),

    # URL para el registro de usuarios
    path('register/', register, name='registro'),  # Cambiado a 'registro'

    # URLs de autenticación
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Otras URLs...
    path('chat/', chat_view, name='chat'),
    path('get_messages/', get_messages, name='get_messages'),
    
    path('', views.home, name='home'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
