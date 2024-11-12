from django.db import models

class Comercio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    categoria = models.CharField(
        max_length=50,
        choices=[
            ('restaurante', 'Restaurante'),
            ('ferreteria', 'Ferretería'),
            ('heladeria', 'Heladería'),
            ('mascotas', 'Tienda de Mascotas'),
            ('tienda', 'Tienda de barrio'),
            ('farmacia', 'Farmacia'),
            ('hotel', 'Hotel')
            
        ]
    )
    direccion = models.CharField(max_length=150, default="Dirección no especificada")
    contacto = models.CharField(max_length=50, default="Sin contacto")
    redes_sociales = models.URLField(blank=True, null=True)
    foto = models.ImageField(upload_to='fotos_comercios/', blank=True, null=True)
    novedad = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre

# comercios/models.py
from django.db import models

class Novedad(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='novedades/', blank=True, null=True)
    fecha_publicacion = models.DateField(auto_now_add=True)
    comercio = models.ForeignKey(Comercio, on_delete=models.CASCADE, related_name="novedades", null=True)

    def __str__(self):
        # Manejo de None para comercio
        comercio_nombre = self.comercio.nombre if self.comercio else "Sin comercio"
        return f"Novedad: {self.titulo} de {comercio_nombre}"

