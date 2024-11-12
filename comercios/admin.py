# comercios/admin.py
from django.contrib import admin
from .models import Comercio, Novedad

# Registra el modelo Comercio con opciones de administración personalizadas
@admin.register(Comercio)
class ComercioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'novedad')  # Mostrar el campo de novedad
    list_filter = ('categoria', 'novedad')

# Registra el modelo Novedad con opciones personalizadas
@admin.register(Novedad)
class NovedadAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'comercio', 'fecha_publicacion')
    search_fields = ('titulo', 'comercio__nombre')
