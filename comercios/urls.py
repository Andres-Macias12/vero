from django.urls import path, include
from .views import (
    lista_comercios,  
    ComercioDetailView,
    ComercioCreateView, ComercioUpdateView, ComercioDeleteView,
    NovedadListView, NovedadDetailView,
    NovedadCreateView, NovedadUpdateView, NovedadDeleteView,
    register  # Asegúrate de importar la vista de registro
)

urlpatterns = [
    # URLs para Comercio
    path('comercios/', lista_comercios, name='comercio-list'),  # Lista de comercios usando lista_comercios
    path('comercios/<int:pk>/', ComercioDetailView.as_view(), name='comercio-detail'),  # Detalle de un comercio
    path('comercios/crear/', ComercioCreateView.as_view(), name='comercio-create'),  # Crear un nuevo comercio
    path('comercios/<int:pk>/editar/', ComercioUpdateView.as_view(), name='comercio-update'),  # Editar un comercio existente
    path('comercios/<int:pk>/eliminar/', ComercioDeleteView.as_view(), name='comercio-delete'),  # Eliminar un comercio

    # URLs para Novedad
    path('novedades/', NovedadListView.as_view(), name='novedad-list'),  # Lista de novedades
    path('novedades/<int:pk>/', NovedadDetailView.as_view(), name='novedad-detail'),  # Detalle de una novedad
    path('novedades/crear/', NovedadCreateView.as_view(), name='novedad-create'),  # Crear una nueva novedad
    path('novedades/<int:pk>/editar/', NovedadUpdateView.as_view(), name='novedad-update'),  # Editar una novedad existente
    path('novedades/<int:pk>/eliminar/', NovedadDeleteView.as_view(), name='novedad-delete'),  # Eliminar una novedad

    # URL para el registro de usuarios
    path('register/', register, name='register'), 
]
