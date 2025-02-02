# Generated by Django 5.1.2 on 2024-10-31 21:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "comercios",
            "0003_remove_comercio_contacto_remove_comercio_direccion_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="comercio",
            name="contacto",
            field=models.CharField(default="Sin contacto", max_length=50),
        ),
        migrations.AddField(
            model_name="comercio",
            name="direccion",
            field=models.CharField(default="Dirección no especificada", max_length=150),
        ),
        migrations.AddField(
            model_name="comercio",
            name="redes_sociales",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="novedad",
            name="comercio",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="novedades",
                to="comercios.comercio",
            ),
        ),
        migrations.AlterField(
            model_name="comercio",
            name="categoria",
            field=models.CharField(
                choices=[
                    ("restaurante", "Restaurante"),
                    ("ferreteria", "Ferretería"),
                    ("heladeria", "Heladería"),
                    ("mascotas", "Tienda de Mascotas"),
                ],
                max_length=50,
            ),
        ),
    ]
